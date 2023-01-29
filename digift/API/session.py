from requests import Session


class APIsession(Session):
    def __init__(self, **kwargs):
        self.base_api_url = kwargs.pop('base_api_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        response = super().request(method, url=f'{self.base_api_url}{url}', **kwargs)
        return response

    def get_js_test_task(self, search: str = None, sort_field: str = None):
        params: dict = {}

        if search:
            params.update({'search': search})
        if sort_field:
            params.update({'sort_field': sort_field})

        return self.request(method='GET', url='/api/js-test-task', params=params)
