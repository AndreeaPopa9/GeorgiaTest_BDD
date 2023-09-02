from behave import *

@given('I am on the Lulu and Georgia sign-in page')
def step_impl(context):
    context.signin_page.open_signin_page()

@when('I enter my email address "{email_address}" and password "{password}"')
def step_impl(context, email_address, password):
    context.signin_page.enter_email(email_address)
    context.signin_page.enter_password(password)

@when('I click on the Sign In button')
def step_impl(context):
    context.signin_page.click_signin_btn()

@then('I am redirected to My Account page')
def step_impl(context):
    context.signin_page.check_my_account_page()

@then('I should see an error message indicating "{error_message}"')
def step_impl(context, error_message):
    context.signin_page.check_signin_error_message(error_message)