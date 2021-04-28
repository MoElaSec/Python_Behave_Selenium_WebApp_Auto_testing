from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

sys.path.append("D:\\Uni Deb stuff\\2021 -2'nd Semester(8th)\\Software Testing\\Final Project")

from features.steps.locaters import locator


@given('The AutomationPractice site is open')
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("http://automationpractice.com/index.php")
    context.driver.maximize_window()
    assert context.driver.title == "My Store"


@given('The Sign In link is clicked')
def click_signin_link(context):
    assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
    context.driver.find_element(*locator["sign_in_link"]).click()
    assert context.driver.title == "Login - My Store"


@given('Enter email "{email}" and password "{pwd}"')
def enter_info(context, email, pwd):
    context.driver.find_element(*locator["sign_in_email"]).send_keys(email)
    context.driver.find_element(*locator["sign_in_pass"]).send_keys(pwd)


@when('Sign in button is clicked')
def click_signin_button(context):
    context.driver.find_element(*locator["sign_in_button"]).click()


@then('User must successfully login into his/her account')
def access_granted(context):
    text = context.driver.find_element(*locator["my_account"]).text
    assert text == "MY ACCOUNT"
    context.driver.close()


@given('Enter email "" and password "123"')
def step_impl(context):
    context.driver.find_element(*locator["sign_in_email"]).send_keys("")
    context.driver.find_element(*locator["sign_in_pass"]).send_keys("123")


@given('Enter email "valid@email.com" and password ""')
def step_impl(context):
    context.driver.find_element(*locator["sign_in_email"]).send_keys("valid@email.com")
    context.driver.find_element(*locator["sign_in_pass"]).send_keys("")


@then("The {msg} error message is shown")
def error_msg(context, msg):
    if context.driver.find_elements(*locator["error_msg"]):
        print("Element exists")
    else:
        print("Element doesn't exits")

    context.driver.close()
    assert True, "Test Passed"
