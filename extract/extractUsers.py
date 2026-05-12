from extract.base_extractor import BaseExtractor

class ExtractUsers(BaseExtractor):

    def extract_users(self):

        return self.base_extractor("users")

