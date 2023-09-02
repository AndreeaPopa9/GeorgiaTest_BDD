Feature: Updating Total Price

  Scenario: Add 2 items and remove one from the cart to verify total price

    Given I am on the Lulu and Georgia page
    When I search the item "Doric Round Dining Table" in the search bar
    And I add it to the cart
    When I search the item "Archer Dining Table" in the search bar
    And I add it to the cart
    Then I open the cart page
    And The total price is the sum of the prices of the items: "Doric Round Dining Table", "Archer Dining Table"
    When I remove the "Archer Dining Table" from the cart
    Then The total price is updated to reflect the price of the remaining item "Doric Round Dining Table"

    Scenario: Add 3 items and remove one from the cart to verify total price

    Given I am on the Lulu and Georgia page
    When I search the item "Vix Dining Chair" in the search bar
    And I add it to the cart
    When I search the item "Sydney Dining Chair" in the search bar
    And I add it to the cart
    When I search the item "Ida Dining Arm Chair" in the search bar
    And I add it to the cart
    Then I open the cart page
    And The total price is the sum of the prices of the items: "Vix Dining Chair", "Sydney Dining Chair", "Ida Dining Arm Chair"
    When I remove the "Ida Dining Arm Chair" from the cart
    Then The total price is updated to reflect the price of the remaining items "Vix Dining Chair", "Sydney Dining Chair"






