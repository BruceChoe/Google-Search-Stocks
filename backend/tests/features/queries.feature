Feature: Owner queries
  As a pet owner
  I should be able to make queries for my lost pets
  So that shelters or animal control can notify me if my pets are found

  Scenario: Make a query
    Given I have not submitted any queries before
    When I submit a query for a brown german shepherd
    Then I should have a single brown german shepherd in my list of queries

  Scenario: View no queries
    Given I have not submitted any queries before
    When I do not submit a query
    Then I should have nothing in my list of queries
