import mysql.connector
from mysql.connector import Error
from config.config import Config


class DataBaseConnection:

    def db_connection(self):

        try :
            connection = mysql.connector.connect(
                host = Config.DB_HOST,
                user = Config.DB_USER,
                password = Config.DB_PASSWORD,
                database = Config.DB_NAME
            )

            if connection.is_connected():

                print("DB Connection Success")

        except Error as e:

            print(f"Error Occurs: {e}")

t = DataBaseConnection()
t.db_connection()
    

