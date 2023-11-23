import os
import numpy as np
from mysql import connector

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, f'../../config/config.ini')


def open_connector():
    from configparser import ConfigParser
    
    config = ConfigParser()
    config.read(config_dir)
    
    conn = connector.connect(
        host=config.get("MySQL", "host"),
        port=config.get("MySQL", "port"),
        user=config.get("MySQL", "user"),
        passwd=config.get("MySQL", "passwd"),
        database=config.get("MySQL", "database")
    )
    
    return conn


# confirmed
def grade_single_values(location_id, value_type, value):
    # create dict
    dict_grade = {}

    # open connector
    conn = open_connector()
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
    conn = open_connector()
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
    count_evacuation = np.logical_and(value >= top_value, value < 1e6).sum(axis=1)
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

    print(dict_grade)
    return dict_grade


# TEST
if __name__ == "__main__":
    
    def generate_matrix(rows, cols, min_value, max_value):
        import numpy as np
        
        matrix = np.zeros((rows, cols))

        for i in range(rows):
            for j in range(cols):
                distance = np.sqrt((i - rows // 2)**2 + (j - cols // 2)**2)
                cell = np.random.randint(min_value, max_value + 1)*(1 - (distance/max(rows, cols))*0.5)
                matrix[i, j] = max(round(cell, 1), 0)

        return matrix

    value = generate_matrix(8, 8, 199, 200)
    
    # params
    location_id = 7
    value_type = "temperature"
    total_cnt = 64
    percentage = 50

    # return dict
    dict = grade_multiple_values(location_id=location_id,
                                       value_type=value_type,
                                       value=value,
                                       total_cnt=total_cnt,
                                       percentage=percentage)
    
    print(dict)
