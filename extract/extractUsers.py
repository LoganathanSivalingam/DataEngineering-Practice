from extract.base_extractor import BaseExtractor

class ExtractUsers(BaseExtractor):

    def extract_users(self):

         try:
            return self.base_extractor("users")
        
         except Exception as e:

            print(f"Status code: {e}")


