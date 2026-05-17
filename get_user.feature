Feature: Get user details from API

  Scenario: Retrieve user with ID 2
    Given the API endpoint is "https://reqres.in/api/users/2"
    When I send a GET request
    Then the response status code should be 200
    And the user id should be 2
