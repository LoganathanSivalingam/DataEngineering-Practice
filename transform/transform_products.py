import pandas as pd 
from extract.extractProducts import ExtractProducts

class TransformProducts():

    def clean_df(self,df):

        df = df.dropna()
        df = df.drop_duplicates()
        df= df[df["product_price"] > 0]
        df.columns = df.columns.str.lower().str.replace(" ","_")
        df["product_title"] = df["product_title"].str.strip() 
        df["product_category"] = df["product_category"].str.replace(" ","_").str.lower()
        df["product_price"] = df["product_price"].astype(float)

        return df
        



    def transform_products(self):

        try:
            extract = ExtractProducts()
            products = extract.extract_products()
        
            products_details = {
                "product_id":[],
                "product_title":[],
                "product_price":[],
                "product_description":[],
                "product_category" :[],
                "product_rating" :[],
                "product_rating_count" :[]
            }
            for product in products:
                products_details["product_id"].append(product["id"])
                products_details["product_title"].append(product["title"])
                products_details["product_price"].append(product["price"])
                products_details["product_description"].append(product["description"])
                products_details["product_category"].append(product["category"])
                products_details["product_rating"].append(product["rating"]["rate"])
                products_details["product_rating_count"].append(product["rating"]["count"])

            df = pd.DataFrame(products_details)

            df = self.clean_df(df)
            
            return df
        
        except Exception as e:
            print(f"Exception : {e}")
            return
    

t = TransformProducts()
print(t.transform_products())