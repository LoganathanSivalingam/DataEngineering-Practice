from etl_pipeline import ETLPipeline
import pandas as pd

class DataTransformer:

    def __init__(self):

        self.etl = ETLPipeline()

        self.data_frames = self.etl.extract()
    

    def clean_data(self):

        cleaned_df = []

        for df in self.data_frames :

            df.fillna(0,inplace=True)
            df.drop_duplicates(inplace=True)
            df.columns = df.columns.str.lower()

            cleaned_df.append(df)

        return cleaned_df
    
    def merge_data(self):

         df = self.clean_data()
         result= pd.merge(df[0],df[1])
         
         return pd.merge(result,df[2])
    

    def feature_engineering(self):

        df = self.clean_data()

        targeted_df = df[1]

        targeted_df["total_spent"] = targeted_df["price"]* targeted_df["quantity"]

        return targeted_df
    

    def aggregate_data(self):

        df = self.clean_data()
        targeted_df = df[1]

        targeted_df["total"] = targeted_df["price"] * targeted_df["quantity"]

        group_by_df = targeted_df.groupby("customer")

        total_orders = group_by_df["order_id"].count()
        total_spent = group_by_df["total"].sum()
        avg_order_value = group_by_df["total"].mean()
        city = group_by_df["city"].first()

        final_df = pd.DataFrame({
            "customer": total_orders.index,
            "city": city.values,
            "total_orders": total_orders.values,
            "total_spent": total_spent.values,
            "avg_order_value": avg_order_value.values
        })

        return final_df






transform = DataTransformer()
print(transform.aggregate_data())

