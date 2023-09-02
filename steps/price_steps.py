from time import sleep

from behave import *

items_prices = {}


@given('I am on the Lulu and Georgia page')
def step_impl(context):
    context.item_page.open_main_page()


@when('I search the item "{item}" in the search bar')
def step_impl(context, item):
    context.item_page.search_for_item(item)
    items_prices.update({item: context.item_page.get_item_price()})


@when('I add it to the cart')
def step_impl(context):
    context.item_page.add_item_to_cart()


@then('I open the cart page')
def step_impl(context):
    context.cart_page.enter_cart_page()


@then('The total price is the sum of the prices of the items: "{item1}", "{item2}", "{item3}"')
def step_impl(context, item1, item2, item3):
    sleep(3)
    context.cart_page.verify_total_price(item1, item2, item3, items_prices=items_prices)


@then('The total price is the sum of the prices of the items: "{item1}", "{item2}"')
def step_impl(context, item1, item2):
    context.cart_page.verify_total_price(item1, item2, items_prices=items_prices)


@when('I remove the "{item}" from the cart')
def step_impl(context, item):
    sleep(3)
    context.cart_page.remove_item_from_cart(item)


@then('The total price is updated to reflect the price of the remaining items "{item1}", "{item2}"')
def step_impl2(context, item1, item2):
    sleep(3)
    context.cart_page.verify_total_price(item1, item2, items_prices=items_prices)


@then('The total price is updated to reflect the price of the remaining item "{item}"')
def step_impl(context, item):
    sleep(3)
    context.cart_page.verify_total_price(item, items_prices=items_prices)
    context.cart_page.remove_item_from_cart(item)
