import random

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import sys

sys.path.append("D:\\Uni Deb stuff\\2021 -2'nd Semester(8th)\\Software Testing\\Final Project")

from features.steps.locaters import locator


# @given('The AutomationPractice site is open')
# def open_website(context):
#     context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     context.driver.implicitly_wait(10)
#     context.driver.get("http://automationpractice.com/index.php")
#     context.driver.maximize_window()
#     assert context.driver.title == "My Store"


# @given('The Sign In link is clicked')
# def click_signin_link(context):
#     assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
#     context.driver.find_element(*locator["sign_in_link"]).click()
#     assert context.driver.title == "Login - My Store"


@given('Enter email "{email}"')
def enter_email(context, email):
    context.driver.find_element(*locator["sign_up_email"]).send_keys(str(random.randint(0, 1000000)) + email)


@when('Create an account button is clicked')
def click_create_account(context):
    context.driver.find_element(*locator["create_account_button"]).click()
    assert context.driver.title == "Login - My Store"


@when('the user wants to create a record with "{gender}" as gender')
def pick_gender(context, gender):
    if gender == "Mr.":
        context.driver.find_element(*locator["gender_radiobutton_mr"]).click()
    else:
        context.driver.find_element(*locator["gender_radiobutton_mrs"]).click()


@when('the user record has a first name of "{fname}" same as address')
def first_name(context, fname):
    context.driver.find_element(*locator["firstname"]).send_keys(fname)


@when('the user record has a last name of "{lname}" same as address')
def last_name(context, lname):
    context.driver.find_element(*locator["lastname"]).send_keys(lname)


@when('Password of "{pwd}"')
def create_password(context, pwd):
    context.driver.find_element(*locator["sign_up_password"]).send_keys(pwd)


@when('Date of Birth of "{dof}"')
def dof(context, dof):
    day = dof[0]
    month = dof[2:4]
    year = dof[5:]

    select = Select(context.driver.find_element(*locator["days_dropdown"]))
    select.select_by_value(day)

    select = Select(context.driver.find_element(*locator["months_dropdown"]))
    select.select_by_value(month)

    select = Select(context.driver.find_element(*locator["years_dropdown"]))
    select.select_by_value(year)


@when('Want to Receive special offers from our partners! and sign-up for News letter')
def optin(context):
    context.driver.find_element(*locator["newsletter_checkbox"]).click()
    context.driver.find_element(*locator["optin_checkbox"]).click()


@when('the Address is "{loc}"')
def address(context, loc):
    context.driver.find_element(*locator["sign_up_address"]).send_keys(loc)


@when('City is "{city}"')
def pick_city(context, city):
    context.driver.find_element(*locator["city"]).send_keys(city)


@when('State is "{state}"')
def pick_state(context, state):
    print("This is State ------>", state)

    select = Select(context.driver.find_element(*locator["state_dropdown"]))
    select.select_by_visible_text(state)


@when('zip code is "{zip_code}"')
def write_zip_code(context, zip_code):
    context.driver.find_element(*locator["postcode"]).send_keys(zip_code)


@when('Country is set to default which is United States')
def step_impl(context):
    assert True, "No need to change country"


@when('Mobile Phone is "{num}"')
def pick_mobile_num(context, num):
    context.driver.find_element(*locator["mobile"]).send_keys(num)


@when('Address ref. is default: My Address')
def step_impl(context):
    assert True, "No need to change Address Reference"


@then('User must successfully create and account with "{acc}" as account name')
def step_impl(context, acc):
    context.driver.find_element(*locator["register_button"]).click()
    assert context.driver.title == "My account - My Store"
    acc_name = context.driver.find_element(*locator["account_name"]).text
    if acc == acc_name:
        assert True, f"This is indeed {acc}"
