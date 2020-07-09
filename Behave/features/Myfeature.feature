Feature:  Orange HRMS logo
  Scenario: Logo presence on Orange HRMS page
    Given launch chromebrowser
    When open orange HRM homepage
    Then veriy logo is present on main page
    And Close browser