Feature: Authentication

  Scenario: Get user info
    When Get user info
    Then Response status should be 200

  Scenario: Create folder
    When Create folder from file create_folders.json
    Then Response status should be 200
