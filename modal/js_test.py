import requests


class Api:
    def __init__(self, base_session):
        self.base_session = base_session

    def api_js(self):
        URL = '/api/js-test-task'
        PARAMS = {"search": "Alcatel", "sort-field": "name"}

        api = requests.get(url=URL, params=PARAMS)

        return api
