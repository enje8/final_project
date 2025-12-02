import allure
from time import sleep
from page.AuthPage import AuthPage
from page.SchedulePage import SchedulePage
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_event(browser):
    
    event_name = str(uuid.uuid4())

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login()

    schedule_page = SchedulePage(browser)
    schedule_page.go()
    schedule_page.add_event(event_name)
    created_event_name = schedule_page.open_event(event_name)
    assert created_event_name == event_name

def test_update_event(browser):
    old_name = str(uuid.uuid4())
    new_name = str(uuid.uuid4())

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login()

    schedule_page = SchedulePage(browser)
    schedule_page.go()

    schedule_page.add_event(old_name)

    schedule_page.update_event(old_name, new_name)

    
    updated_event_name = schedule_page.open_event(new_name)
    assert updated_event_name == new_name


def test_delete_event(browser):
    
    event_name = str(uuid.uuid4())

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login()

    schedule_page = SchedulePage(browser)
    schedule_page.go()
    schedule_page.add_event(event_name)
    schedule_page.open_event(event_name)
    schedule_page.delete_event()

    schedule_page.element_deleted(event_name)


def test_add_description(browser):
    desc = str(uuid.uuid4())
    event_name = str(uuid.uuid4())

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login()

    schedule_page = SchedulePage(browser)
    schedule_page.go()

    schedule_page.add_event_with_description(event_name, desc)

    new_desc = schedule_page.get_description(event_name)
    assert desc == new_desc


def test_add_event_yellow(browser):
    
    event_name = str(uuid.uuid4())

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login()

    schedule_page = SchedulePage(browser)
    schedule_page.go()
    schedule_page.add_event_with_yellow_color(event_name)

    color = schedule_page.get_color(event_name)
    assert color == "rgba(250, 198, 65, 1)"

