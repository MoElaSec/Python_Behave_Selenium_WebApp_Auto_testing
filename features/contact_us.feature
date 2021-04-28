Feature: AutomationPractice contact us page test

  Background:
    Given The AutomationPractice site is open
    And The Contact us link is clicked

  Scenario Outline: Successfully contacting AutomationPracitce.
    Given The "<msg>" is written in Message field.
    And The Email is  "<parameter>"
    And Subject is "<subject>"
    And Attached file is "<attached>"
    When Send button is clicked
    Then The "<output>" message is shown.
    Examples:
      | parameter                | msg                | attached    | subject          | output                                               |
      | valid123@email.com       | Goedmorgen.        | \image.png  | Customer service | Your message has been successfully sent to our team. |
      | Halo@gmail.com           | this is my problem |             | Webmaster        | Your message has been successfully sent to our team. |
      | salam@email.com          | how are you?       |             | Customer service | Your message has been successfully sent to our team. |
      | annyeonghaseyo@email.com | how are you?       | \image2.png | Customer service | Your message has been successfully sent to our team. |


  Scenario Outline: Failed to contact AutomationPracitce.
    Given The "<msg>" is written in Message field.
    And The Email is  "<parameter>"
    And Subject is "<subject>"
    When Send button is clicked
    Then The "<output>" message is shown.
    Examples:
      | parameter         | msg      | subject          | output                                          |
      | valid@email.com   |          | Customer service | The message cannot be blank.                    |
      | invalid.email.com | Bonjure! | Webmaster        | Invalid email address.                          |
      | valid@email.com   | test     |                  | Please select a subject from the list provided. |
      | valid@email.com   |          |                  `| The message cannot be blank.                    |