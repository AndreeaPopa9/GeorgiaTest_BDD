from behave import *
import random

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
month = months[random.randint(0, 11)]
day = str(random.randint(1, 31))
birthday = month + " " + day


@given('I am logged into the Lulu and Georgia website')
def step_impl(context):
    context.signin_page.signin()


@when('I click on the Edit button')
def step_impl(context):
    context.my_account_page.click_edit_btn()


@when('I select my date of birth')
def step_impl(context):
    context.my_account_page.select_date_of_birth(month, day)


@when('I click on the Update account button')
def step_impl(context):
    context.my_account_page.click_update_btn()


@then('My date of birth should be displayed in My Account page')
def step_impl(context):
    context.my_account_page.check_updated_birth(birthday)

@then('I logout from the page')
def step_impl(context):
    context.my_account_page.logout_btn()


