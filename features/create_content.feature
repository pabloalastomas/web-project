Feature: Create Content
  In order to keep track of what content I want to see and what I have seen,
  As a user
  I want to create the content together with the review and status

  Background: There is a registered user
    Given Exists a user "user" with password "webproject"

  Scenario: Create the content status
    Given I login as user "user" with password "webproject"
    When I create the status
      | film           |  | status    |
      | Coco           |  | Watching  |
      | Doctor Strange |  | Favourite |
    Then I'm viewing the status created for content by "user"
      | film           |  | status    |
      | Coco           |  | Watching  |
      | Doctor Strange |  | Favourite |
    And There are 2 content in DB.

  Scenario: Create the content review
    Given I login as user "user" with password "webproject"
    When I create the review
      | film           |  | status    |  | review                  |
      | Coco           |  | Watching  |  | Amazing film!           |
      | Doctor Strange |  | Favourite |  | I love Sorcerer Supreme |
    Then I'm viewing the review created for content by "user"
      | film           |  | status    |  | review                  |
      | Coco           |  | Watching  |  | Amazing film!           |
      | Doctor Strange |  | Favourite |  | I love Sorcerer Supreme |

  Scenario: Create rating