Feature: Edit Content
  In order to keep updated my previous registers about the content
  As a user
  I want to edit a content register I created

  Background: There is a registered user
    Given Exists a user "user" with password "webproject"
    And Exists streaming platforms
      | platform           |
      | Disney +           |
      | Netflix            |
      | HBO                |
      | Amazon Prime Video |
    And Exist content registered by "user"
      | film           |  | status    |  | rating |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  | 5      |  | Amazing !               |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | Doctor Strange |  | Favourite |  | 5      |  | I love Sorcerer Supreme |  | Disney + |  | https://cutt.ly/eb0z5Gs |


  @edit_status
  Scenario: Edit content status
    Given I login as user "user" with password "webproject"
    When I edit the status
      | film           |  | status  |
      | Inception      |  | Pending |
      | Doctor Strange |  | Watched |
    Then I'm viewing the content status of the "user"
      | film           |  | status  |
      | Inception      |  | Pending |
      | Doctor Strange |  | Watched |

  @edit_review
  Scenario: Edit content review
    Given I login as user "user" with password "webproject"
    When I edit the review
      | film           |  | review        |
      | Inception      |  | Incredible    |
      | Doctor Strange |  | I love MARVEL |
    Then I'm viewing the content review of the "user"
      | film           |  | review        |
      | Inception      |  | Incredible    |
      | Doctor Strange |  | I love MARVEL |

  @edit_rating
  Scenario: Edit content rating
    Given I login as user "user" with password "webproject"
    When I edit the rating
      | film           |  | rating |
      | Inception      |  | 2      |
      | Doctor Strange |  | 4      |
    Then I'm viewing the content rating of the "user"
      | film           |  | rating |
      | Inception      |  | 2      |
      | Doctor Strange |  | 4      |
