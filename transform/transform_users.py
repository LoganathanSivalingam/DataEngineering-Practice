import pandas as pd 
from extract.extractUsers import ExtractUsers

class TransformUsers:

    def clean_df(self,df):

        df = df.dropna()
        df = df.drop_duplicates()
        df.columns = df.columns.str.lower().str.replace(" ","_")
        df["user_name"] = df["user_name"].str.strip() 

        return df

    def transform_users(self):

        try:
            extract = ExtractUsers()
            users = extract.extract_users()

            users_details = {
                "user_id" : [],
                "user_name":[],
                "user_phone":[],
                "user_city":[],
                "user_email":[]
            }

            for user in users:
                users_details["user_id"].append(user["id"])
                users_details["user_name"].append(user["username"])
                users_details["user_phone"].append(user["phone"])
                users_details["user_city"].append(user["address"]["city"])
                users_details["user_email"].append(user["email"])

            df = pd.DataFrame(users_details)
            df = self.clean_df(df)
            
            return df
        
        except Exception as e:
            print(f"Exception : {e}")
            return
        
t = TransformUsers()
print(t.transform_users())

