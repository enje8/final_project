import allure
import pytest
from selenium import webdriver
from api.SkyengApi import SkyengApi
from DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api() -> SkyengApi:
        return SkyengApi(DataProvider().get("apiUrl"), DataProvider().get("token"))