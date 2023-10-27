import os
import numpy as np
import sqlite3


current_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(current_dir, f'../../database/sensor.db')


def grade_multiple(location_id, value_type, value, total_cnt, percentage):
    # create dict
    dict = {}

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
    dict["type_id"] = returned[2]
    dict["type_name"] = returned[3]

    # inspection
    count_inspection = np.logical_and(value >= 0, value <= bottom_value).sum(axis=1)
    count_total_inspection = 0
    for row in count_inspection:
        count_total_inspection += row

    # evacuation
    count_evacuation = np.logical_and(value >= bottom_value, value <= top_value).sum(axis=1)
    count_total_evacuation = 0
    for row in count_evacuation:
        count_total_evacuation += row

    # create value:grade
    if count_total_evacuation >= total_cnt*percentage*0.01:
        dict["grade"] = "evacuation"
    elif count_total_inspection + count_total_evacuation >= total_cnt*percentage*0.01:
        if count_total_evacuation >= total_cnt*percentage*0.01:
            dict["grade"] = "evacuation"
        else:
            dict["grade"] = "inspection"
    else:
        dict["grade"] = "normal"

    return dict


# TEST
if __name__ == "__main__":
    # params
    location_id = 7
    value_type = "temperature"
    value = np.random.randint(0, 71, (8, 8))
    total_cnt = 64
    percentage = 50

    # return dict
    dict = grade_multiple(location_id=location_id,
                                       value_type=value_type,
                                       value=value,
                                       total_cnt=total_cnt,
                                       percentage=percentage)
    
    print(dict)