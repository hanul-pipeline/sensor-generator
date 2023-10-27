import os
import numpy as np
import sqlite3


current_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(current_dir, f'../../database/sensor.db')


def grade_single_values(location_id, value_type, value):
    # create dict
    dict = {}

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
    dict["type_id"] = returned[0]
    dict["type_name"] = returned[1]
    dict["grade"] = returned[2]

    return dict


# TEST
if __name__ == "__main__":
    # params
    location_id = 10
    value_type = "CH4"
    value = 1.5

    # return dict
    dict = grade_single_values(location_id=location_id,
                               value_type=value_type,
                               value=value)
    print(dict)