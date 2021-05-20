Feature: Delete Content
  In order to keep updated my previous registers about the content
  As a user
  I want to delete a content register I created

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

  @delete_content
  Scenario: Delete content
    Given I login as user "user" with password "webproject"
    When I delete the content
      | film           |
      | Inception      |
      | Doctor Strange |
    Then I'm viewing not exist the content of the "user"
      | film           |
      | Inception      |
      | Doctor Strange |

    @delete_link
    Scenario: Delete Platform link
      Given I login as user "user" with password "webproject"
      When I delete the platform link
      | film           |
      | Inception      |
      | Doctor Strange |
      Then I'm viewing not exist the platform link of the "user"