import mysql.connector
from flask import request

from utilities.db.db_manager import dbManager


def fetch_query(query, dbManage = None):
   return dbManager.fetch(query)



def all_comments_by_email(email):
    return "select * from contactus where email= '%s';" % email


def insert_comment_function(email, phone_number, frequency, text):
    query = "INSERT INTO contactus(email, phone_number,frequency,text) VALUES ('%s', '%s', '%s','%s')" % (email,phone_number, frequency, text)
    dbManager.commit(query)


def delete_comment_function(serial_number):
    query ="DELETE FROM contactus WHERE serial_number='%s';" % serial_number
    dbManager.commit(query)


def update_comment_func(frequency, phone_number, text, serial_number):
    query = "UPDATE contactus " \
            "Set frequency = '%s'" \
            ",phone_number='%s'" \
            ",text='%s' where serial_number = '%s';" % (frequency, phone_number, text, serial_number)
    dbManager.commit(query)