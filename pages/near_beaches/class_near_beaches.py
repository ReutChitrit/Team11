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


# ------------------- NEAR BEACHES--------------------------------

def beaches_with_LG_and_SS(city):
    return "select * FROM beaches WHERE city='%s' and surf_store=True and with_life_guard=True;" % city


def beaches_with_SS(city):
    return "select * FROM beaches WHERE city='%s' and surf_store=True;" % city


def beaches_with_LG(city):
    return "select * FROM beaches WHERE city='%s' and with_life_guard=True;" % city


def beaches_by_city(city):
    return "select * FROM beaches WHERE city='%s';" % city


def display_all_beaches():
    return "select * FROM beaches"
