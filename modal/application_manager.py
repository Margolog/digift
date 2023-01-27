from modal.certificates import Certificates
from modal.js_test import Api


class ApplicationManager:
    def __init__(self):
        self.certificate = Certificates()
        self.api_js = Api()
