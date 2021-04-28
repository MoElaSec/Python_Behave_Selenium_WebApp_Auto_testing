from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)
from features.steps.locaters import locator


@given('The Women link is clicked.')
def nav_page(context):
    assert context.driver.find_element(*locator["women_link"]).is_displayed()
    context.driver.find_element(*locator["women_link"]).click()
    assert context.driver.title == "Women - My Store"


@when('the clothes "{page}" sub-page is clicked')
def tops_page(context, page):
    if page == "Tops":
        assert context.driver.find_element(*locator["tops_link"]).is_displayed()
        context.driver.find_element(*locator["tops_link"]).click()
        assert context.driver.title == "Tops - My Store"


@when('The "{sub_cat}" Subcategory is chosen.')
def all_tops_dresses(context, sub_cat):
    if sub_cat == "T-shirts":
        context.driver.find_element(*locator["t-shirts_link"]).click()
    elif sub_cat == "Blouses":
        context.driver.find_element(*locator["blouses_link"]).click()


@then('The "{top}" should show in the "{page}".')
def tops_catgs(context, top, page):
    if page == "Tops":
        if top == "T-shirts":  # for the first scenario_out
            context.driver.find_element(*locator["t-shirts_link"]).is_displayed()

            if context.driver.find_element(*locator["Faded_Short_Sleeve_T-shirts"]).text == top:  # for the second scenario_out
                assert context.driver.find_element(*locator["Faded_Short_Sleeve_T-shirts"]).text == top

        elif top == "Blouses":
            context.driver.find_element(*locator["blouses_link"]).is_displayed()

            if context.driver.find_element(*locator["Blouse"]).text == top:  # for the second scenario_out
                assert context.driver.find_element(*locator["Blouse"]).text == top
