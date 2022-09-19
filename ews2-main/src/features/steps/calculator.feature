Feature: Test Calculator Functionality

Scenario: Addition
    Given Calculator app is running
    When I input 2 + 3 
    Then I get result 5


Scenario: Subtraction
    Given Calculator app is running
    When I input "4" - "1"
    Then I get result 3


    