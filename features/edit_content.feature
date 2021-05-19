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
      | film           |  | status    |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  | Amazing !               |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | Doctor Strange |  | Favourite |  | I love Sorcerer Supreme |  | Disney + |  | https://cutt.ly/eb0z5Gs |