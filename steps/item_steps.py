from behave import *

@given('I search for the item "{item}" in the search bar')
def step_impl(context, item):
    context.item_page.search_for_item(item)

@when('I add the item to cart')
def step_impl(context):
    context.item_page.add_item_to_cart()

@then('The cart icon shows there is one item in the cart')
def step_impl(context):
    context.cart_page.check_number_items_in_cart("1")

@when('I enter the cart page')
def step_impl(context):
    context.cart_page.enter_cart_page()

@then('The item "{item}" is displayed in the cart')
def step_impl(context, item):
    context.cart_page.check_item_in_cart(item)

@when('I remove the item "{item}" from the cart')
def step_impl(context, item):
    context.cart_page.remove_item_from_cart(item)

@then('I should see the success message: "{message}"')
def step_impl(context, message):
    context.cart_page.check_successful_message(message)
