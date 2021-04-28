Feature: AutomationPractice dresses page test

  Background:
    Given The AutomationPractice site is open
    And The Dresses link is clicked

  Scenario Outline: Checking all types of dresses
    When the "<page>" sub-page is clicked.
    Then  "<dress>" should appear in the "<page>".
    Examples:
      | page            | dress                 |
      | Casual Dresses  | Printed Dress         |
      | Evening Dresses | Printed Dress         |
      | Summer Dresses  | Printed Summer Dress  |
      | Summer Dresses  | Printed Chiffon Dress |
