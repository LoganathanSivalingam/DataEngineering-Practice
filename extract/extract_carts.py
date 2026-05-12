from extract.base_extractor import BaseExtractor

class ExtractCarts(BaseExtractor):

    def extract_carts(self):

        return self.base_extractor("carts")

