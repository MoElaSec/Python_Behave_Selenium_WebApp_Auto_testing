Feature: AutomationPractice web page Logo

  Scenario: Logo is presence on AutomationPractice Home Page
    Given Launch a chrome browser
    When YourLogo site is opened
    Then Verify that the logo present on the page
    And Close browser

  Scenario Outline: Logo is presence on AutomationPractice pages
    Given Launch a chrome browser
    When YourLogo site is opened
    Then Navigate to the "<page>" page.
    And Verify that the logo present on the page
    And Close browser
    Examples:
      | page       |
      | contact-us |
      | sign-in    |
      | Dresses    |
      | Women      |

