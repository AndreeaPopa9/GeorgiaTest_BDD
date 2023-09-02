Feature: Filtering Products

  Scenario: Filter products by Bed Size
    Given I search for the category "Beds"
    When I select "Queen" filter option
    Then I see the filter selected on the page as: "Bed Size: Queen"

   Scenario: Filter products by Color
    Given I search for the category "Pillows"
    When I select "Orange" filter option
    Then I see the filter selected on the page as: "Color: Orange"

   Scenario: Filtering products by multiple criteria
    Given I search for the category "Outdoor"
    When I select "Furniture" filter option
    And I select "Stone" filter option
    Then I see the filters selected on the page as: "Product Type: Furniture", "Material: Stone"



























