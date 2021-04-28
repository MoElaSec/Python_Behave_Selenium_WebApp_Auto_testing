from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)
from features.steps.locaters import locator


@given('The Dresses link is clicked')
def nav_page(context):
    assert context.driver.find_element(*locator["dresses_link"]).is_displayed()
    context.driver.find_element(*locator["dresses_link"]).click()
    assert context.driver.title == "Dresses - My Store"


@when('the "{page}" sub-page is clicked.')
def dress_page(context, page):
    if page == "Casual Dresses":
        assert context.driver.find_element(*locator["casual_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["casual_dresses_link"]).click()
        assert context.driver.title == "Casual Dresses - My Store"
    if page == "Evening Dresses":
        assert context.driver.find_element(*locator["evening_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["evening_dresses_link"]).click()
        assert context.driver.title == "Evening Dresses - My Store"
    if page == "Summer Dresses":
        assert context.driver.find_element(*locator["summer_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["summer_dresses_link"]).click()
        assert context.driver.title == "Summer Dresses - My Store"


@then('"{dress}" should appear in the "{page}".')
def pick_dress(context, dress, page):
    if page == "Casual Dresses":
        assert context.driver.find_element(*locator["casual_printed_dress"]).text == dress
    elif page == "Evening Dresses":
        assert context.driver.find_element(*locator["evening_printed_dress"]).text == dress
    elif page == "Summer Dresses":
        if context.driver.find_element(*locator["printed_summer_dress"]).text == dress:
            assert True, "It's Printed Summer Dress"
        else:
            assert context.driver.find_element(*locator["printed_chiffon_dress"]).text == dress
