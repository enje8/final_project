from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataProvider import DataProvider


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.skyeng.ru/login"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login(self):

        # Ожидаем появления поля ввода логина
        (
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "js-send-otp-form-to-username-password")
                )
            )
        )

        (
            self.__driver.find_element(
                By.CLASS_NAME, "js-send-otp-form-to-username-password"
            ).click()
        )

        (
            self.__driver.find_element(By.NAME, "username").send_keys(
                DataProvider().get("email")
            )
        )
        (
            self.__driver.find_element(By.NAME, "password").send_keys(
                DataProvider().get("password")
            )
        )
        (
            self.__driver.find_element(
                By.CLASS_NAME, "js-username-password-form-button"
            ).click()
        )

        # Ожидаем появления логотипа
        # (убеждаемся, что главная страница полностью загружена)
        (
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "greeting"))
            )
        )

    def get_current_url(self):
        return self.__driver.current_url
