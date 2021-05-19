Feature: Create Content
  In order to keep track of what content I want to see and what I have seen,
  As a user
  I want to create the content together with the review and status

  Background: There is a registered user
    Given Exists a user "user" with password "webproject"

  @create_status
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

  @create_review
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

  @create_rating
  Scenario: Create the content rating
    Given I login as user "user" with password "webproject"
    When I create the rating
      | film           |  | status    |  | rating |
      | Coco           |  | Watched   |  | 4      |
      | Doctor Strange |  | Favourite |  | 5      |
    Then I'm viewing the rating created for content by "user"
      | film           |  | status    |  | rating |
      | Coco           |  | Watched   |  | 4      |
      | Doctor Strange |  | Favourite |  | 5      |

  @create_link
  Scenario: Create the content platform link
    Given I login as user "user" with password "webproject"
    And Exists streaming platforms
      | platform           |
      | Disney +           |
      | Netflix            |
      | HBO                |
      | Amazon Prime Video |
    Then I create the platform link
      | film           |  | link                    |  | platform |
      | Doctor Strange |  | https://cutt.ly/eb0z5Gs |  | Disney + |
      | Inception      |  | https://cutt.ly/Xb0xy0m |  | Netflix  |
    Then I'm viewing the platform link created for content by "user"
      | film           |  | link                    |  | platform |
      | Doctor Strange |  | https://cutt.ly/eb0z5Gs |  | Disney + |
      | Inception      |  | https://cutt.ly/Xb0xy0m |  | Netflix  |