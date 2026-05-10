from db_manager import DataBaseManager

class ETLPipeline():

    def __init__(self):

        self.db = DataBaseManager("localhost","py_sql","root","root")
        self.db.connect()

    def extract(self):

        if self.db.connection.is_connected():
        
            customers_df = self.db.fetch_table("customers")
            orders_df = self.db.fetch_table("orders")
            payments_df = self.db.fetch_table("payments")

            return customers_df , orders_df , payments_df

# etl = ETLPipeline()
# print(etl.extract())