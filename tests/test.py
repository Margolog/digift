from selene import command, be, have
from selene.support.shared import browser

from modal import app


def test_open():
    app.given_opened_page()

    # browser.open("http://@qa.digift.ru/") #вынести в конфитест,вынести переменные и енв http://HR:test@qa.digift.ru/
    # browser.element('.par-options__button').perform(command.js.scroll_into_view)

    browser.element('[data-value="500"]').click()
    browser.element('[data-value="500"]').should(be.enabled)
    browser.element('[value="500"]').should(be.present)


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

