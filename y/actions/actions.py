from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
import datetime
import pandas as pd
from datetime import datetime, timedelta
import pytz

global member_id
#
# def connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="admin",
#         database="rasa_chatbot"
#     )
#     mydb = connection.cursor()
#
#     return mydb
#
member_id_list = []

class EmailID(Action):

    def name(self) -> Text:
        return "member_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="rasa_chatbot"
        )
        # connection()
        mydb = connection.cursor()
        member_id_list.clear()
        member_id = tracker.latest_message['text']
        print(member_id)
        member_id_list.append(member_id)
        print("member_id_list", member_id_list)

        select_qry = "SELECT email_id FROM cust_info_tbl where id = "+ member_id +";"
        mydb.execute(select_qry)
        myresult = mydb.fetchall()[0][0]
        # myresult = fetch_id(member_id)


        # DataUpdate(member_id)
        dispatcher.utter_message(text=myresult)
        # mydb.commit()

        return []

class Validity(Action):

    def name(self) -> Text:
        return "validity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="rasa_chatbot"
        )
        mydb = connection.cursor()
        confirmation = tracker.latest_message['text']
        print(confirmation)

        # curent_date = datetime.datetime.now()
        curent_date = datetime.utcnow()
        # week_ago = curent_date + datetime.timedelta(days=7)
        week_ago = datetime.now(tz=pytz.utc) + timedelta(days=7)
        week_ago = week_ago.strftime("%Y:%m:%d %H:%M:%S")
        # print("week ago", week_ago)
        # str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))


        validity_qry = "UPDATE cust_info_tbl SET validity = "+ week_ago +" WHERE id = "+ member_id_list[0] +";"
        print(validity_qry)
        # val = (week_ago)
        mydb.execute(validity_qry)
        # connection.commit()

        # myresult = mydb.fetchall()[0][0]


        dispatcher.utter_message(text='Data Inserted')
        # mydb.commit()

        return []