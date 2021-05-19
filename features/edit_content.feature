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
  Scenario: Edit status content
    Given I login as user "user" with password "webproject"
    When I edit the status content
      | film           |  | status    |
      | Inception      |  | Pending   |
      | Doctor Strange |  | Watched |