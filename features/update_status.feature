Feature: Update Status
  In order to keep track of what content I want to see and what I have seen,
  As a user
  I want to update the status of the content.

  Background: There is a registered user
    Given Exists a user "user" with password "webproject"

  Scenario: Update the content status
    Given I login as user "user" with password "webproject"
    When I update the status
      | film                  |  | status   |
      | Star Wars: Episode IV |  | Watching |
    Then I'm viewing the status update for content by "user"
      | film                  |  | status   |
      | Star Wars: Episode IV |  | Watching |
    And The content has a status