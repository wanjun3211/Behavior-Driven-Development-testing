# Behavior-Driven-Development Testing

## Introduction

This is a very small project, and I was trying to use the concept of Behavior Driven Development concept to test a simple API. Python Benhave framework was implemented.

## Project structure

The folder structure should adhere to the following shown as it is the requirement of Behave framework. In the project folder, there should be a folder called features with steps folder inside. And get_user_steps.py can use other name but it should be python file that import requrests library and behave framework.   

Another import file should include the .feathure file, which is using the **plain text**(** Given, When, Then style**) to describe the scenerio needing to be test.

![Behave stucture](/images/behaveTesting.png "Behave pic")




## Coding explanation. 

1. Project purpose

   This is just to test API, address https://reqres.in/api/users/2, and make it in a understandable way using the plain text. In the file ended with .feature, it is has a very clear description about the scenario

**Feature: Get user details from API**

**Scenario: Retrieve user with ID 2**   
**Given the API endpoint is "https://reqres.in/api/users/2"**    
**When I send a GET request**     
**Then the response status code should be 200**    
**And the user id should be 2**

  
2. Python file in steps folder

    
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
  

5. Get a single book

      Using the  **Get** to list all the book information. The script in this section is
```javascript
   pm.test("Status code is 200",  ()=> {
    pm.response.to.have.status(200);
});

const response = pm.response.json();
console.log(response['current-stock']);

pm.test("Stock is greater than 0",  ()=> {
    pm.expect(response['current-stock']).to.be.above(0);
});
   ```
   
7. Order book

    Using the **Post** to show one book information. The script in this section is
   ```javascript
    pm.test("Status code is 201",  ()=> {
    pm.response.to.have.status(201);
   });
    ```
    
9. Get all order books

    Using the **Get** to show all the book order information. The script in this section is
```javascript
    pm.test("Status code is 200",  ()=> {
    pm.response.to.have.status(200);
});

const response = pm.response.json();
console.log(response[0].id);
pm.globals.set("orderID", response[0].id);
```
   
11. Get an order

     Using the **Get** to show one order information.
    
13. Update an order

    Using the **Patch** to update the order information. In this instance, I tried to update the borrower's name. The script in this section is
```javascript
    pm.test("Status code is 204",  ()=> {
    pm.response.to.have.status(204);
});
```
    
     
15. Delete order

    Using the **Delete** to delete an existing order. The script in this section is
    ```javascript
    pm.test("Status code is 204",  ()=> {
    pm.response.to.have.status(204);
    });
    ```

    
## Using **Runner** to automate this collection

The photo is a screenshot that shows this collection result. And there is one fialed API request due to repetitive registration of client.

<img width="1234" height="823" alt="image" src="https://github.com/user-attachments/assets/9672aa1c-4d28-48e8-947a-aac42819288f" />

## Other feature of this API testing 

The base API address and book ID has been stored in the varible.

<img width="619" height="655" alt="image" src="https://github.com/user-attachments/assets/89a043e1-595a-4087-ae96-92c31d3a58a1" />
