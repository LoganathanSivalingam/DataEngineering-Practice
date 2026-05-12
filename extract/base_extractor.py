import requests
from config.config import Config

class BaseExtractor:

    def base_extractor(self,path):

        self.path = path
        endpoint = f"{Config.API_BASE_URL}/{self.path}"

        try:
            res = requests.get(endpoint)
            if res.status_code == 200:
                return res.json()
            
            else :
                raise Exception(f"Status Code :{res.status_code}")
            
        except Exception as e:
            print(f"Exception:{e}")      
        
        return []

