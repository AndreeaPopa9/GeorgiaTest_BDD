Feature: Account Management

  Scenario: Update Account Information
    Given I am logged into the Lulu and Georgia website
    When  I click on the Edit button
    And I select my date of birth
    And I click on the Update account button
    Then My date of birth should be displayed in My Account page
    And I logout from the page



