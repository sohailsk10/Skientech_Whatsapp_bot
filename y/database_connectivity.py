# import mysql.connector
# from mysql.connector import Error
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="admin",
#     database="rasa_chatbot"
# )
# print(mydb)
#
#
# def update_sql(sql_query):
#     mycursor = mydb.cursor()
#     mycursor.execute(sql_query)
#     myresult = mycursor.fetchall()[0][0]
#     mydb.commit()
#     return myresult
#
#
# # return myresult
#
# # member_id = tracker.latest_message['text']
# # print(member_id)
# def fetch_id(member_id):
#     select_qry = "SELECT email_id FROM cust_info_tbl where id = " + member_id + ";"
#     # select_qry = "SELECT email_id FROM cust_info_tbl where id = 1;"
#     print(select_qry)
#     abc = update_sql(select_qry)
#     print(abc)
#     return abc
#
#     # fetch_id()
#
# # abc = update_sql(select_qry)
# # myresult = abc.fetchall()
# # print(myresult)
# # fetch_id()


import datetime
import pandas as pd

curent_date = datetime.datetime.now()
week_ago = curent_date + datetime.timedelta(days=7)
print(pd.to_datetime(curent_date))
print(week_ago)