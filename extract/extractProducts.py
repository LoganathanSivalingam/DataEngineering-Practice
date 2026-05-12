from extract.base_extractor import BaseExtractor

class ExtractProducts(BaseExtractor):

    def extract_products(self):

        return self.base_extractor("products")

