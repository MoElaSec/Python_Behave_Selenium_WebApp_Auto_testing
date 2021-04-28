Feature: AutomationPractice Tops page test

  Background:
    Given The AutomationPractice site is open
    And The Women link is clicked.

  Scenario Outline: Checking all types of Tops.
    When the clothes "<page>" sub-page is clicked
    Then  The "<top>" should show in the "<page>".
    Examples:
      | page | top    |
      | Tops | T-shirts |
      | Tops | Blouses  |

  Scenario Outline: Checking T-Shirts & Blouses.
    When the clothes "<page>" sub-page is clicked
    And The "<sub_cat>" Subcategory is chosen.
    Then  The "<top>" should show in the "<page>".
    Examples:
      | page | sub_cat  | top                       |
      | Tops | T-shirts | Faded Short Sleeve T-shirts |
      | Tops | Blouses  | Blouse                      |