# Behavior-Driven-Development Testing

## Introduction

This is a very small project, and I was trying to use the concept of Behavior Driven Development concept to test a simple API. Python Benhave framework was implemented.

## Project structure

The folder structure should adhere to the following shown as it is the requirement of Behave framework. In the project folder, there should be a folder called features with steps folder inside. And get_user_steps.py can use other name but it should be python file that import requrests library and behave framework.   

Another import file should include the .feathure file, which is using the **plain text**(** Given, When, Then style**) to describe the scenerio needing to be test.

![Behave stucture](/images/behaveTesting.png "Behave pic")




## Coding explanation. 

### 1. Project purpose

This is just to test API, address https://reqres.in/api/users/2, and make it in a understandable way using the plain text. In the file ended with .feature, it is has a very clear description about the scenario

>**Feature: Get user details from API**

>**Scenario: Retrieve user with ID 2**   
>**Given the API endpoint is "https://reqres.in/api/users/2"**    
>**When I send a GET request**     
>**Then the response status code should be 200**    
>**And the user id should be 2**

  
### 2. Python file in steps folder

    
```python

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
```

