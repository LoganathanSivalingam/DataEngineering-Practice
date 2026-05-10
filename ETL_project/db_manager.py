import mysql.connector
from mysql.connector import Error
import pandas as pd

class DataBaseManager:

    def __init__(self,host,database,user,password):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None


    # connection
    def connect(self):
         
        try :
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user ,
                database = self.database,
                password = self.password
            )

            if self.connection.is_connected:

                self.cursor = self.connection.cursor()

            print("Connection Success")

        except Error as e:
            print(f"Error occurs: {e}")



    # fetch table
    def fetch_table(self,table_name):

        if self.connection.is_connected:
            
            try:
                query = f"SELECT * FROM {table_name}"
                
                self.cursor.execute(query)

                data = self.cursor.fetchall()

                columns = [i[0] for i in self.cursor.description]

                df = pd.DataFrame(data, columns = columns)

              
                return df 

            except Exception as e:
                print(f"Error occurs: {e}")
    

    def execute_query(self,query):
        
        if self.connection.is_connected():
            
            try:
                query = query 

                self.cursor.execute(query)
                result = self.cursor.fetchall()

                return result
    
            except Exception as e:
                print(f"Error occurs (execute_query) : {e}")

    def close(self):

        if self.connection.is_connected():
            self.connection.close()
            print("Connection Closed")



# db = DataBaseManager("localhost","py_sql","root","root")
# db.connect()
# print(db.fetch_table("orders"))
# db.execute_query("SELECT * FROM orders LIMIT 2;")
# db.close()
    