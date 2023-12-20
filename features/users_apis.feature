Feature: Users API cases using POM model

  @smoke
  Scenario: Get the users details
    Given the user gather the end url 'https://reqres.in/api/users'
    When the user send the API Get request
    Then api response status code should be 200
    And the user api response text contains '12'


  @test2
  Scenario: Create the users record
    Given the user gather the end url 'https://reqres.in/api/users?page=2'
    When the user pass the below data to send POST API
      | name     | job    |
      | morpheus | leader |
    Then api response status code should be 201
    And the user api response text contains 'morpheus'

  @test3
  Scenario: Update the users record-PUT
    Given the user gather the end url 'https://reqres.in/api/users/2'
    When the user pass the below data to send PUT API
      | updated_name | updated_job |
      | ram          | automation  |
    Then api response status code should be 200
    And the user api response text contains 'ram'

  @test4
  Scenario: Delete the user record
    Given the user gather the end url 'https://reqres.in/api/users/20'
    When the user send the delete api request
    Then api response status code should be 204

