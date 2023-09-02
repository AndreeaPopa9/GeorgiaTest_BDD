Feature: Test the functionality to add and remove one item from the cart

  Scenario: Add and remove item from the shopping cart
    Given I search for the item "Landry Indoor / Outdoor Sofa" in the search bar
    When I add the item to cart
    Then The cart icon shows there is one item in the cart
    When I enter the cart page
    Then The item "Landry Indoor / Outdoor Sofa" is displayed in the cart
    When I remove the item "Landry Indoor / Outdoor Sofa" from the cart
    Then I should see the success message: "Shopping cart is empty"




