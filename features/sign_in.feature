Feature: AutomationPractice sign in page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Sign in to AutomationPractice with valid credential
    Given Enter email "s2@gmail.com" and password "12345"
    When Sign in button is clicked
    Then User must successfully login into his/her account


  Scenario Outline: Fail Sign-In
    Given Enter email "<parameter>" and password "<password>"
    When Sign In button is clicked
    Then The "<msg>" error message is shown
    Examples:
      | parameter         | password | msg                        |
      |                   | 123      | An email address required. |
      | invalid.email.com | 12345    | Invalid email address.     |
      | valid@email.com   |          | Password is required.      |
      |                   |          | An email address required. |