import allure
from selene import be
from selene.support.shared import browser


class Certificates:
    def click_on_the_500(self):
        with allure.step('Choose 500'):
            browser.element('[data-value="500"]').click()
        return self

    def checx_active_500(self):
        with allure.step('Checx value 500'):
            browser.element('[data-value="500"]').should(be.enabled)
        return self

    def checx_value_500(self):
        with allure.step('Checx value 500'):
            browser.element('[value="500"]').should(be.present)
        return self



    browser.element('[data-value="1000"]').click()
    browser.element('[data-value="1000"]').should(be.enabled)
    browser.element('[value="1000"]').should(be.present)


    browser.element('[data-value="2000"]').click()
    browser.element('[data-value="2000"]').should(be.enabled)
    browser.element('[value="2000"]').should(be.present)


    browser.element('[data-value="3000"]').click()
    browser.element('[data-value="3000"]').should(be.enabled)
    browser.element('[value="3000"]').should(be.present)

    browser.element('[data-value="5000"]').click()
    browser.element('[data-value="5000"]').should(be.enabled)
    browser.element('[value="5000"]').should(be.present)


    browser.element('[data-value="10000"]').click()
    browser.element('[data-value="10000"]').should(be.enabled)
    browser.element('[value="10000"]').should(be.present)

