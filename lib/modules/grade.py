import os
import numpy as np
import sqlite3


current_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(current_dir, f'../../database/sensor.db')


# confirmed
def grade_single_values(location_id, value_type, value):
    # create dict
    dict_grade = {}

    # open connector
    conn = sqlite3.connect(database=database_dir)
    cursor = conn.cursor()

    # get values
    QUERY = f"""
		SELECT type_id, type_name, grade
        FROM grade
		WHERE location_id = '{location_id}'
		AND value_type = '{value_type}'
		AND '{value}' BETWEEN bottom_value AND top_value
    """
    cursor.execute(QUERY)
    returned = cursor.fetchall()[0]

    # create value: type id, type name, grade
    dict_grade["type_id"] = returned[0]
    dict_grade["type_name"] = returned[1]
    dict_grade["grade"] = returned[2]

    return dict_grade


# confirmed
def grade_multiple_values(location_id, value_type, value, total_cnt, percentage):
    # create dict
    dict_grade = {}

    # open connector
    conn = sqlite3.connect(database=database_dir)
    cursor = conn.cursor()

    # get params
    QUERY = f"""
    SELECT bottom_value, top_value, type_id, type_name
    FROM grade
    WHERE location_id = '{location_id}'
    AND value_type = '{value_type}'
    AND grade = 'inspection'
    """
    cursor.execute(QUERY)
    returned = cursor.fetchall()[0]
    bottom_value = returned[0]
    top_value = returned[1]

    # close connector
    conn.close()

    # create value: type id, type name
    dict_grade["type_id"] = returned[2]
    dict_grade["type_name"] = returned[3]

    # inspection
    count_inspection = np.logical_and(value >= bottom_value, value <= top_value).sum(axis=1)
    count_total_inspection = 0
    for row in count_inspection:
        count_total_inspection += row

    # evacuation
    count_evacuation = np.logical_and(value >= top_value, value <= top_value).sum(axis=1)
    count_total_evacuation = 0
    for row in count_evacuation:
        count_total_evacuation += row

    # create value:grade
    if count_total_evacuation >= total_cnt*percentage*0.01:
        dict_grade["grade"] = "evacuation"
    elif count_total_inspection + count_total_evacuation >= total_cnt*percentage*0.01:
        if count_total_evacuation >= total_cnt*percentage*0.5*0.01:
            dict_grade["grade"] = "evacuation"
        else:
            dict_grade["grade"] = "inspection"
    else:
        dict_grade["grade"] = "normal"

    return dict_grade


# TEST
if __name__ == "__main__":
    # params
    location_id = 7
    value_type = "temperature"
    value = np.random.randint(0, 71, (8, 8))
    total_cnt = 64
    percentage = 50

    # return dict
    dict = grade_multiple_values(location_id=location_id,
                                       value_type=value_type,
                                       value=value,
                                       total_cnt=total_cnt,
                                       percentage=percentage)
    
    print(dict)

    # params
    location_id = 10
    value_type = "CH4"
    value = 2.5

    # return dict
    dict = grade_single_values(location_id=location_id,
                               value_type=value_type,
                               value=value)
    print(dict)