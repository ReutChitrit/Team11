import mysql.connector

from utilities.db.db_manager import dbManager


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='group11')
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


def fetch_func(query):
    return dbManager.fetch(query)


def display_all_cities():
    return "select * FROM city_location"


def display_certain_cities(city):
    return "select latitude, longitude FROM city_location WHERE city='%s';" % city
