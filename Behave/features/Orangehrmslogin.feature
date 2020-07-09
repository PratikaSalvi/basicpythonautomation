Feature: Orange HRMS login
  Scenario: Login to orange HRMS with vaid parameter
    Given Browser used should be Chrome Browser
    When I open HRMS Homepage
    And Enter username "admin" and password "admin123"
    And Click on Login Button
    Then User should get Logged In and land on Dashboard

  Scenario Outline: Login to OrangeHRMS with Multiple Parameters
    Given I launch Chrome Browser
    When I open Orange HRM homepage
    And Enter username "<username>" and password "<password">
    And Click on Login Button
    Then User should get Logged In and land on Dashboard


    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |


