
import allure
from allure_commons.types import Severity
from pytest_voluptuous import S

from tests.Shema.shema import js


def test_api_js_test_task(base_session):

    result = base_session.get(url='/api/js-test-task',
                              params={'search': 'Alcatel', 'sort_field': 'name'})

    assert result.json()['name'] == 'name'
    assert result.json() == S(js)

