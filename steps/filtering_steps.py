from time import sleep

from behave import *

@given('I search for the category "{category}"')
def step_impl(context, category):
    context.item_page.search_for_item(category)

@when('I select "{filter}" filter option')
def step_impl(context, filter):
    sleep(2)
    context.item_page.filter_items(filter)

@then('I see the filter selected on the page as: "{filter}"')
def step_impl(context,filter):
    context.item_page.verify_filter_on_page(filter)

@then('I see the filters selected on the page as: "{filter1}", "{filter2}"')
def step_impl(context,filter1, filter2):
    sleep(2)
    context.item_page.verify_filter_on_page(filter1)
    context.item_page.verify_filter_on_page(filter2)









