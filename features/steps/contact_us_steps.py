import parse
from hamcrest import assert_that, equal_to
from behave import given, when, then, step, register_type


# To enable eampty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from features.steps.locaters import locator


@given('The Contact us link is clicked')
def step_given_send_msg_into_responder(context):
    assert context.driver.find_element(*locator["contact_us"]).is_displayed()
    context.driver.find_element(*locator["contact_us"]).click()
    assert context.driver.title == "Contact us - My Store"


@step('The "{msg:NullableString}" is written in Message field.')
def step_impl(context, msg):
    context.driver.find_element(*locator["contact_message"]).send_keys(msg)


@step('The Email is  "{parameter}"')
def step_impl(context, parameter):
    context.driver.find_element(*locator["contact_email"]).send_keys(parameter)


@step('Subject is "{subject:NullableString}"')
def step_impl(context, subject):
    if subject == "Webmaster":
        subject = 1
    elif subject == "Customer service":
        subject = 2
    else:
        subject = 0

    select = Select(context.driver.find_element(*locator['subject_heading']))
    select.select_by_value(str(subject))


@step('Attached file is "{attached:NullableString}"')
def step_impl(context, attached):
    print("check this Out --------->", attached, os.getcwd())
    if attached:
        context.driver.find_element(*locator["attach_file_button"]).send_keys(os.getcwd() + "\\features\\steps" + attached)
    else:
        assert True, "No file to attach"


@when('Send button is clicked')
def send_msg(context):
    context.driver.find_element(*locator["submit_message_contact"]).click()


@then('The "{output}" message is shown.')
def step_impl(context, output):
    try:
        succ_response = context.driver.find_element(*locator["succ_contact_msg"]).text
        assert succ_response == output, f"{output}"
    except:
        fail_msg = context.driver.find_element(*locator["fail_contact_msg"]).text
        assert fail_msg == output, f"{output}"
    finally:
        context.driver.close()
