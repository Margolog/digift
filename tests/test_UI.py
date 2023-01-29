import allure
import pytest
from selene import command
from selene.support.shared import browser

from digift.UI.application_manager import ApplicationManager


@pytest.fixture(scope='function', autouse=True)
def open_start_page(browser_management):

    browser.open('')
    browser.element('.par-options__button').perform(command.js.scroll_into_view)

    yield

    browser.quit()


@allure.feature('Кнопка с номиналом карты 500')
def test_choose_500(app: ApplicationManager):

    app.certificate.click_on_the_500()

    app.certificate.check_value_500()\
        .check_active_500()


@allure.feature('Кнопка с номиналом карты 1000')
def test_choose_1000(app: ApplicationManager):

    app.certificate.click_on_the_1000()

    app.certificate.check_value_1000()\
        .check_active_1000()


@allure.feature('Кнопка с номиналом карты 2000')
def test_choose_2000(app: ApplicationManager):

    app.certificate.click_on_the_2000()

    app.certificate.check_value_2000()\
        .check_active_2000()


@allure.feature('Кнопка с номиналом карты 3000')
def test_choose_3000(app: ApplicationManager):

    app.certificate.click_on_the_3000()

    app.certificate.check_value_3000()\
        .check_active_3000()



@allure.feature('Кнопка с номиналом карты 5000')
def test_choose_5000(app: ApplicationManager):

    app.certificate.click_on_the_5000()

    app.certificate.check_value_5000()\
        .check_active_5000()


@allure.feature('Кнопка с номиналом карты 1000')
def test_choose_10000(app: ApplicationManager):

    app.certificate.click_on_the_10000()

    app.certificate.check_value_10000()\
        .check_active_10000()

