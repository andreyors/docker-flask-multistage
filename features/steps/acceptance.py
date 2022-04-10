from __future__ import annotations

from behave import given, then, when
from requests import session


@given("we have web server started")
def step_impl1(context):
    pass


@when('we do a HTTP request to "{url}"')
def step_impl2(context, url):
    context.response = session().get(url)


@then('we receive "{message}"')
def step_impl3(context, message):
    assert context.response.status_code == 200
    assert context.response.text == message
