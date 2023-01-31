import os

from dotenv import load_dotenv
from selene.support.shared import browser
from digift.UI.application_manager import ApplicationManager
import pytest

from digift.API.session import APIsession


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    load_dotenv


@pytest.fixture(scope='session')
def browser_management():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser.config.base_url = f'http://{login}:{password}@qa.digift.ru/'

    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 900


@pytest.fixture(scope='function')
def app() -> ApplicationManager:
    _app = ApplicationManager()
    return _app


@pytest.fixture(scope='session')
def base_session() -> APIsession:
    with APIsession(base_api_url='https://www.lenvendo.ru') as session:
        yield session


