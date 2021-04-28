Feature: AutomationPractice sign up page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Create a User using valid data
    Given Enter email "example_email123@email.com"
    When Create an account button is clicked
    And the user wants to create a record with "Mr." as gender
    And the user record has a first name of "Jhon" same as address
    And the user record has a last name of "Smith" same as address
    And Password of "12345"
    And Date of Birth of "3-11-1998"
    And Want to Receive special offers from our partners! and sign-up for News letter
    And the Address is "Example street 19"
    And City is "San Francisco"
    And State is "Washington"
    And zip code is "12345"
    And Country is set to default which is United States
    And Mobile Phone is "9876654"
    And Address ref. is default: My Address
    Then User must successfully create and account with "Jhon Smith" as account name

  Scenario Outline: Create a User using valid data
    Given Enter email "<email>"
    When Create an account button is clicked
    And the user wants to create a record with "<gender>" as gender
    And the user record has a first name of "<fname>" same as address
    And the user record has a last name of "<lname>" same as address
    And Password of "<passwd>"
    And Date of Birth of "<dob>"
    And Want to Receive special offers from our partners! and sign-up for News letter
    And the Address is "<address>"
    And City is "<city>"
    And State is "<state>"
    And zip code is "<zip-code>"
    And Country is set to default which is United States
    And Mobile Phone is "<mobile>"
    And Address ref. is default: My Address
    Then User must successfully create and account with "<acc>" as account name
    Examples:
      | email            | gender | fname  | lname      | acc               | passwd  | dob       | address            | city          | state      | zip-code | mobile  |
      | cpp@email.com    | Mr.    | bjarne | stroustrup | bjarne stroustrup | 5678910 | 1-12-1950 | Example street 15  | San Francisco | California | 00000    | 5876657 |
      | java@email.com   | Mr.    | james  | gosling    | james gosling     | 5978910 | 8-10-1955 | Example street 139 | Los Angeles   | New York   | 67890    | 9676687 |
      | python@email.com | Mrs.   | guido  | rossum     | guido rossum      | 5678999 | 1-11-1956 | Example street 8   | San Diego     | Washington | 12345    | 3876656 |
      | perl@email.com   | Mr.    | larry  | wall       | larry wall        | 3278910 | 9-10-1954 | Example street 10  | San Jose      | California | 11111    | 1276654 |


