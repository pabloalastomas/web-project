Feature: Update Status
In order to keep track of what content I want to see and what I have seen,
As a user
I want to update the status of the content.
    Background: There is a registered user
    Given Exists a user "user" with password "password"

#  Scenario: Update the content status
#    Given I login as user "user" with password "password"
#    When I update status
#      | status      |
#      | Watching    |
#    Then I'm viewing the status update for content by "user"
#      | status      |
#      | Watching    |
#    And The content has a status