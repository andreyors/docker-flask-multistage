import requests
from behave import *

@given("we have web server started")
def step_impl(context):
    pass

@when('we do a HTTP request to "{url}"')
def step_impl(context, url):
    context.response = requests.session().get(url)

@then('we receive "{message}"')
def step_impl(context, message):
    assert context.response.status_code == 200
    assert context.response.text == message

