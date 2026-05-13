import pandas as pd
from extract.extract_carts import ExtractCarts

class TransformCarts:

    def clean_df(self,df):

        df = df.dropna()
        df = df.drop_duplicates()
        df.columns = df.columns.str.lower().str.replace(" ","_")

        return df

    def transform_carts(self):

        try:

            extract = ExtractCarts()
            carts = extract.extract_carts()
            
            carts_details = {
                "cart_id" : [],
                "user_id" : [],
                "date" : [],
                "product_id":[],
                "product_quantity":[]
            }

            for cart in carts:
                
                for product in cart["products"]:
                    carts_details["cart_id"].append(cart["id"])
                    carts_details["user_id"].append(cart["userId"])
                    carts_details["date"].append(cart["date"])


                    carts_details["product_id"].append(product["productId"])
                    carts_details["product_quantity"].append(product["quantity"])

            df = pd.DataFrame(carts_details)
            df = self.clean_df(df)
            return df
        
        except Exception as e:

            print(f"Exception : {e}")

t = TransformCarts()
print(t.transform_carts())


