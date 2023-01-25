import os
from dotenv import load_dotenv
from selene import command
from selene.support.shared import browser
from modal.application_manager import ApplicationManager
import pytest
from utils.base import BaseSession


@pytest.fixture(scope='session', autouse='true')
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def browser_management():

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    browser.config.base_url = f'http://{login}:{password}@qa.digift.ru/'

    browser.open('/')
    browser.element('.par-options__button').perform(command.js.scroll_into_view)

    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 900

    yield




@pytest.fixture(scope='function')
def app() -> ApplicationManager:
    _app = ApplicationManager()
    return _app



@pytest.fixture(scope='session')
def base_session():
    with BaseSession(base_api_url='https://www.lenvendo.ru') as session:
        yield session

