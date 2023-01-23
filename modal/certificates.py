import allure
from selene import be
from selene.support.shared import browser


class Certificates:
    def click_on_the_500(self):
        with allure.step('Choose 500'):
            browser.element('[data-value="500"]').click()
        return self

    def check_active_500(self):
        with allure.step('Check value 500'):
            browser.element('[data-value="500"]').should(be.enabled)
        return self

    def check_value_500(self):
        with allure.step('Check value 500'):
            browser.element('[value="500"]').should(be.present)
        return self

    def click_on_the_1000(self):
        with allure.step('Choose 1000'):
            browser.element('[data-value="1000"]').click()
        return self

    def check_active_1000(self):
        with allure.step('Check value 1000'):
            browser.element('[data-value="1000"]').should(be.enabled)
        return self

    def check_value_1000(self):
        with allure.step('Check value 1000'):
            browser.element('[value="1000"]').should(be.present)
        return self



    def click_on_the_2000(self):
        with allure.step('Choose 2000'):
            browser.element('[data-value="2000"]').click()
        return self

    def check_active_2000(self):
        with allure.step('Check value 2000'):
            browser.element('[data-value="2000"]').should(be.enabled)
        return self

    def check_value_2000(self):
        with allure.step('Check value 2000'):
            browser.element('[value="2000"]').should(be.present)
        return self



    def click_on_the_3000(self):
        with allure.step('Choose 3000'):
            browser.element('[data-value="3000"]').click()
        return self

    def check_active_3000(self):
        with allure.step('Check value 3000'):
            browser.element('[data-value="3000"]').should(be.enabled)
        return self

    def check_value_3000(self):
        with allure.step('Check value 3000'):
            browser.element('[value="3000"]').should(be.present)
        return self


    def click_on_the_5000(self):
        with allure.step('Choose 5000'):
            browser.element('[data-value="5000"]').click()
        return self

    def check_active_5000(self):
        with allure.step('Check value 5000'):
            browser.element('[data-value="5000"]').should(be.enabled)
        return self

    def check_value_5000(self):
        with allure.step('Check value 5000'):
            browser.element('[value="5000"]').should(be.present)
        return self

    def click_on_the_10000(self):
        with allure.step('Choose 10000'):
            browser.element('[data-value="10000"]').click()
        return self

    def check_active_10000(self):
        with allure.step('Check value 10000'):
            browser.element('[data-value="10000"]').should(be.enabled)
        return self

    def check_value_10000(self):
        with allure.step('Check value 10000'):
            browser.element('[value="10000"]').should(be.present)
        return self

