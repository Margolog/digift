from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_api_url = kwargs.pop('base_api_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_api_url}{url}', **kwargs)


class JsTestTask:
    def __init__(self, name, image, price):
        self.name = 'Alcatel'
        self.image = image
        self.price = price
