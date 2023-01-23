from selene import command, be, have
from selene.support.shared import browser
from modal.application_manager import ApplicationManager



def test_open(app: ApplicationManager):
    app.main.open_page()
    (
        app.certificate.click_on_the_500()

        .checx_value_500()
        .checx_active_500()
     )

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

