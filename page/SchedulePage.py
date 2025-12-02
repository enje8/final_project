from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SchedulePage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.skyeng.ru/login"
        self.__driver = driver

    def go(self):
        (
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-qa-id="left-menu-item:Расписание"]'
            ).click()
        )

    @allure.step("Добавить событие")
    def add_event(self, name):
        self.__driver.find_element(By.CLASS_NAME, "add-icon").click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Личное событие')]"
        ).click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]"
        ).send_keys(name)
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Cохранить')]"
        ).click()

    @allure.step("Открыть событие")
    def open_event(self, name):
        (
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{name}')]")
                )
            )
        )
        self.__driver.find_element(
            By.XPATH, f"//*[contains(text(), '{name}')]"
        ).click()
        (
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "popup-header")
                )
            )
        )
        return self.__driver.find_element(By.CLASS_NAME, "popup-header").text

    @allure.step("Изменить название")
    def update_event(self, old_name, new_name):
        (
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{old_name}')]")
                )
            )
        )
        self.__driver.find_element(
            By.XPATH, f"//*[contains(text(), '{old_name}')]"
        ).click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Редактировать')]"
        ).click()
        (
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "popup-header")
                )
            )
        )
        self.__driver.find_element(
            By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]"
        ).clear()
        self.__driver.find_element(
            By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]"
        ).send_keys(new_name)
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Cохранить')]"
        ).click()
        sleep(1)

    @allure.step("Удалить событие")
    def delete_event(self):
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Удалить')]"
        ).click()

    @allure.step("Удалено событие")
    def element_deleted(self, name):
        (
            WebDriverWait(self.__driver, 10).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{name}')]")
                )
            )
        )

    @allure.step("Добавить событие с описанием")
    def add_event_with_description(self, name, description):
        self.__driver.find_element(By.CLASS_NAME, "add-icon").click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Личное событие')]"
        ).click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]"
        ).send_keys(name)
        self.__driver.find_element(
            By.XPATH,
            "//textarea[contains(@placeholder, 'ссылка на вебинар')]",
        ).clear()
        self.__driver.find_element(
            By.XPATH,
            "//textarea[contains(@placeholder, 'ссылка на вебинар')]",
        ).send_keys(description)
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Cохранить')]"
        ).click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Cохранить')]"
        ).click()

    @allure.step("Получить описание события")
    def get_description(self, name):
        (
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{name}')]")
                )
            )
        )
        self.__driver.find_element(
            By.XPATH, f"//*[contains(text(), '{name}')]"
        ).click()
        (
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "popup-header")
                )
            )
        )
        sleep(4)
        return self.__driver.find_element(
            By.CSS_SELECTOR, ".popup-body .description"
        ).text

    @allure.step("Добавить событие с желтым цветом")
    def add_event_with_yellow_color(self, name):
        self.__driver.find_element(By.CLASS_NAME, "add-icon").click()
        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Личное событие')]"
        ).click()
        sleep(3)
        self.__driver.find_element(
            By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]"
        ).send_keys(name)

        circles = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.color-circle")
            )
        )

        circles[1].click()

        self.__driver.find_element(
            By.XPATH, "//*[contains(text(), 'Cохранить')]"
        ).click()

    @allure.step("Проверка желтого цвета")
    def get_color(self, name):
        (
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{name}')]")
                )
            )
        )
        self.__driver.find_element(
            By.XPATH, f"//*[contains(text(), '{name}')]"
        )

        event_block = self.__driver.find_element(
            By.XPATH,
            f"//*[contains(text(), '{name}')]/ancestor::div["
            "contains(@class, 'event-block__container')]",
        )

        color = event_block.value_of_css_property("border-left-color")
        return color
