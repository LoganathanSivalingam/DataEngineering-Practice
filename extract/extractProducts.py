from extract.base_extractor import BaseExtractor

class ExtractProducts(BaseExtractor):

    def extract_products(self):

          try:
            return self.base_extractor("products")
        
          except Exception as e:

            print(f"Status code: {e}")


