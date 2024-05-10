@api
Feature: Authentication

  Scenario: Get user info
    Given I am logged in user
    When GET USER info
    Then Status code is equal 200
    And Values 'user', 'username' in body are equal 'Yosyp Voloshchuk'

  Scenario: Create folder
    When Create Folder
    Then Status code is equal 200
