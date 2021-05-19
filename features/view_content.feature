Feature: View content
  In order to keep track of what content I want to see and what I have seen,
  As a user
  I want to view the content created

  Background: There are 2 users registered with content created
    Given Exists a user "user1" with password "webproject"
    And Exists a user "user2" with password "webproject"
    And Exists streaming platforms
      | platform           |
      | Disney +           |
      | Netflix            |
      | HBO                |
      | Amazon Prime Video |
    And Exist content registered by "user1"
      | film           |  | status    |  | rating |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  |       5|  | Amazing !               |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | Doctor Strange |  | Favourite |  |       5|  | I love Sorcerer Supreme |  | Disney + |  | https://cutt.ly/eb0z5Gs |
    And Exist content registered by "user2"
      | film           |  | status    |  | rating |  | review                  |  | platform |  | link                    |
      | Inception      |  | Watched   |  |       4|  | Incredible !            |  | Netflix  |  | https://cutt.ly/Xb0xy0m |
      | TENET          |  | Favourite |  |       5|  | Good but confusing      |  | Disney + |  | https://cutt.ly/eb0z5Gs |

  Scenario: View the list of content created by the user
    Given I login as user "user1" with password "webproject"
    Then I'm viewing the list of content
      | film           |
      | Inception      |
      | Doctor Strange |

  Scenario: View the global rating of a specific content
    Given I login as user "user1" with password "webproject"
    Then I'm viewing the global rating for the content
      | film           |  | global rating |
      | Inception      |  |            4.5|

  Scenario: View the platform and link added by other user for a specific content
    Given I login as user "user1" with password "webproject"
    Then I'm viewing the platform added by an other user for a specific content
      | film           |  | platform |
      | TENET          |  | Disney + |
    And I'm viewing the link added by an other user for a specific content
      | film           |  | link                    |
      | TENET          |  | https://cutt.ly/eb0z5Gs |

