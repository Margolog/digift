import os

from selene import have, command
from selene.support.shared import browser



def given_opened_page():

    browser.open('http://qa.digift.ru')
    browser.element('.par-options__button').perform(command.js.scroll_into_view)