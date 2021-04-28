from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)
from features.steps.locaters import locator


@given('Launch a chrome browser')
def lunch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)


@when('YourLogo site is opened')
def open_home_page(context):
    context.driver.get("http://automationpractice.com/index.php")
    context.driver.maximize_window()


@then('Navigate to the "{page}" page.')
def nav_page(context, page):
    if page == "contact-us":
        assert context.driver.find_element(*locator["contact_us"]).is_displayed()
        context.driver.find_element(*locator["contact_us"]).click()
        assert context.driver.title == "Contact us - My Store"
    if page == "sign-in ":
        assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
        context.driver.find_element(*locator["sign_in_link"]).click()
        assert context.driver.title == "Login - My Store"
    if page == "Dresses":
        assert context.driver.find_element(*locator["dresses_link"]).is_displayed()
        context.driver.find_element(*locator["dresses_link"]).click()
        assert context.driver.title == "Dresses - My Store"
    if page == "Women":
        assert context.driver.find_element(*locator["women_link"]).is_displayed()
        context.driver.find_element(*locator["women_link"]).click()
        assert context.driver.title == "Women - My Store"


@then('Verify that the logo present on the page')
def verify_logo(context):
    assert context.driver.find_element(*locator["logo"]).is_displayed()


@then('Close browser')
def close_browser(context):
    context.driver.close()
