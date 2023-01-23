import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

@pytest.fixture(scope='session', autouse='true')
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    browser.config.base_url = f'http://{login}:{password}@qa.digift.ru/'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 900

    yield




