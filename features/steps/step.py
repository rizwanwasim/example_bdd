# steps/step.py

from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('launch chrome browser')
def given_launch_chrome_browser(context):
    # context.browser = webdriver.Chrome()
    context.driver = webdriver.Chrome()
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()
@when('Open ornagehrm Homepage')
def when_open_orange_hrm_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that the logo is Present')
def then_verify_that_the_logo_presense_on_page(context):
    logo = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='app']//div//div//div//div//div//div//img[@alt='orangehrm-logo']"))
    )
    assert logo is not None
@then('close the browser')
def and_close_browser(context):
    context.driver.quit()