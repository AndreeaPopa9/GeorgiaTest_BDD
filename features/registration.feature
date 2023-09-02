Feature: Registration to Lulu and Georgia page

  Scenario: Failed registration with email already taken error
    Given I am on the Lulu and Georgia registration page
    When I input "Andreea" in the first name field and "Popa" in the last name field
    And I input my email in the email address field
    And I insert my password in the password and confirmation password fields
    And I deselect the subscription to the newsletter button
    And I click on the Create account button
    Then I should see an error message: "Email has already been taken"