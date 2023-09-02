from browser import Browser
from pages.my_account_page import MyAccount_page
from pages.registration_page import Registration_page
from pages.signin_page import Signin_page
from pages.item_page import Item_page
from pages.cart_page import Cart_page
def before_all(context):
    context.browser = Browser()
    context.registration_page = Registration_page()
    context.signin_page = Signin_page()
    context.my_account_page = MyAccount_page()
    context.item_page = Item_page()
    context.cart_page = Cart_page()

def after_all(context):
    context.browser.close()