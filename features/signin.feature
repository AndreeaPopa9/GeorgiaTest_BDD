Feature: User Sign-in

  Background:
    Given I am on the Lulu and Georgia sign-in page

  @successful
  Scenario: Successful sign-in with valid credentials
    When I enter my email address "andreeapopa9793@gmail.com" and password "TestingPass9%"
    And I click on the Sign In button
    Then I am redirected to My Account page


  @unsuccessful
  Scenario Outline: Unsuccessful sign-in with invalid credentials
    When I enter my email address "<email>" and password "<password>"
    And I click on the Sign In button
    Then I should see an error message indicating "<error_message>"

    Examples:
      | email                     |  | password      | error_message                |
      | andreea97@gmail.com       |  | TestingPass9% | Incorrect email or password. |
      | andreeapopa9793@gmail.com |  | wrongpass     | Incorrect email or password. |
      | andreea9@gmail.com        |  | wrongpass     | Incorrect email or password. |



