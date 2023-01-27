import requests
from modal.application_manager import ApplicationManager
from modal.js_test import Api



def test_api_js_test_task(app: ApplicationManager):

    result = requests.get(app.api_js)

    assert result.status_code == 200
    # assert result.json()['name'] == name
