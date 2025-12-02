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
        (self.__driver.find_element(By.CSS_SELECTOR, '[data-qa-id="left-menu-item:Расписание"]').click())

    def add_event(self):
        (self.__driver.find_element(By.CLASS_NAME, "add-icon").click())

    @allure.step("Добавить событие")
    def add_event(self, name):
        self.__driver.find_element(By.CLASS_NAME,'add-icon').click()
        self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Личное событие')]").click()
        self.__driver.find_element(By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]").send_keys(name)
        self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Cохранить')]").click()
        
    @allure.step("Открыть событие")
    def open_event(self, name):
        (WebDriverWait(self.__driver, 10).
          until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{name}')]"))))
        self.__driver.find_element(By.XPATH, f"//*[contains(text(), '{name}')]").click()
        (WebDriverWait(self.__driver, 10).until(
          EC.visibility_of_element_located((By.CLASS_NAME, 'popup-header'))))
        return self.__driver.find_element(By.CLASS_NAME, 'popup-header').text

    @allure.step("Изменить название")
    def update_event(self, old_name, new_name):
        (WebDriverWait(self.__driver, 10).
          until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{old_name}')]"))))
        self.__driver.find_element(By.XPATH, f"//*[contains(text(), '{old_name}')]").click()
        self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Редактировать')]").click()
        (WebDriverWait(self.__driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'popup-header'))))
        self.__driver.find_element(By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]").clear()
        self.__driver.find_element(By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]").send_keys(new_name)
        self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Cохранить')]").click()
        sleep(1)
    
    @allure.step("Удалить событие")
    def delete_event(self):
        # self.__driver.find_element(By.CLASS_NAME,'add-icon').click()
        # self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Личное событие')]").click()
        # self.__driver.find_element(By.XPATH, "//*[contains(@placeholder, 'посмотреть вебинар')]").send_keys(name)
        # self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Cохранить')]").click()
        # (WebDriverWait(self.__driver, 10).
        #   until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{name}')]"))))
        # self.__driver.find_element(By.XPATH, f"//*[contains(text(), '{name}')]").click()
        self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Удалить')]").click() 

    @allure.step("Удалено событие")
    def element_deleted(self, name):
      (WebDriverWait(self.__driver, 10).until(EC.invisibility_of_element_located((By.XPATH, f"//*[contains(text(), '{name}')]"))))
