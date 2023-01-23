
from selene import have, command
from selene.support.shared import browser


class MainPage:
    def open_page(self):

        browser.open('http://HR:test@qa.digift.ru/')
        browser.element('.par-options__button').perform(command.js.scroll_into_view)

        return self

