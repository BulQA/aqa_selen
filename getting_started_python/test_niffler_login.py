from selene import browser, have, by, be
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()

def test_aliexpress_login():

    """Импортируем данные для авторизации str"""
    a_login = os.getenv("ali_login")
    a_pass = os.getenv("ali_password")

    """Проверяем наличие данных в файле"""
    assert a_login, "ali_login is not set in .env"
    assert a_pass, "ali_password is not set in .env"

    browser.open('https://tr.aliexpress.com/')
    menu = browser.element('.my-account--text--2Yt_prE').should(be.visible)
    menu.hover()
    browser.element(by.text('Giriş yap')).should(be.visible).click()
    browser.element('[aria-label="E-posta"]').should(be.visible).type(a_login).press(Keys.ENTER)
    browser.element('[aria-label="Devam"]').should(be.enabled).click()
    browser.element('[name="fm-login-password"]').should(be.visible).type(a_pass)

def test_internet_herokuapp():
    browser.open('https://the-internet.herokuapp.com/login')
    browser.element('#username').type('tomsmith')
    browser.element('#password').type('SuperSecretPassword!')
    browser.element('button[type="submit"]').click()
    browser.element('#flash').should(have.text('You logged into a secure area!'))