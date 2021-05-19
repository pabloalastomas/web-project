# Created by pepes at 19/05/2021
Feature: View content
  In order to keep track of what content I want to see and what I have seen,
  As a user
  I want to view the content created

  Background: There is a registered user
    Given Exists a user "user" with password "webproject"
    And Exists streaming platforms
      | platform           |
      | Disney +           |
      | Netflix            |
      | HBO                |
      | Amazon Prime Video |
    And Exist content registered by "user"
      | film           |  | status    |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  | Amazing !               |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | Doctor Strange |  | Favourite |  | I love Sorcerer Supreme |  | Disney + |  | https://cutt.ly/eb0z5Gs |
    Then I'm viewing the status created for "user" by content
      | film           |  | status    |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  | Amazing !               |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | Doctor Strange |  | Favourite |  | I love Sorcerer Supreme |  | Disney + |  | https://cutt.ly/eb0z5Gs |
