import requests
from behave import given, when, then

@given('the API endpoint is "{url}"')
def step_given_endpoint(context, url):
    context.url = url

@when('I send a GET request')
def step_when_get_request(context):
    context.response = requests.get(context.url)

@then('the response status code should be {status_code:d}')
def step_then_status_code(context, status_code):
    print("Actual status:", context.response.status_code)
    print("Response body:", context.response.text)
    assert context.response.status_code == status_code

@then('the user id should be {user_id:d}')
def step_then_user_id(context, user_id):
    json_data = context.response.json()
    assert json_data["data"]["id"] == user_id
