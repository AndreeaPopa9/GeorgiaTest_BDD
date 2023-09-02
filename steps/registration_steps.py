from behave import *


@given('I am on the Lulu and Georgia registration page')
def step_impl(context):
    context.registration_page.open_registration_page()

@when('I input "{firstname}" in the first name field and "{lastname}" in the last name field')
def step_impl(context, firstname, lastname):
    context.registration_page.input_firstname(firstname)
    context.registration_page.input_lastname(lastname)

@when('I input my email in the email address field')
def step_impl(context):
    context.registration_page.input_email(context.signin_page.email_address)

@when('I insert my password in the password and confirmation password fields')
def step_impl(context):
    context.registration_page.input_password(context.signin_page.password)

@when('I deselect the subscription to the newsletter button')
def step_impl(context):
    context.registration_page.deselect_subscription()

@when('I click on the Create account button')
def step_impl(context):
    context.registration_page.click_create_account_btn()

@then('I should see an error message: "{error_message}"')
def step_impl(context, error_message):
    context.registration_page.check_registration_error_message(error_message)

