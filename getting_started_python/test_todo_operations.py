from selene import browser, have, be
from selenium.webdriver import Keys


def test_complete_todo():
    browser.open('/')
    browser.element('.new-todo').should(be.blank)

    browser.element('.new-todo').type('a').press(Keys.ENTER)
    browser.element('.new-todo').type('b').press(Keys.ENTER)
    browser.element('.new-todo').type('c').press(Keys.ENTER)

    browser.all('.todo-list>li').should(have.size(3))
