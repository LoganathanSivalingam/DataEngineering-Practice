from extract.base_extractor import BaseExtractor

class ExtractCarts(BaseExtractor):

    def extract_carts(self):

        try:
            return self.base_extractor("carts")
        
        except Exception as e:

            print(f"Status code: {e}")

