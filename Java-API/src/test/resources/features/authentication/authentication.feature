@folders
Feature: Authentication

  @example
  Scenario: Get user info
    When Get user info
    Then Response status should be 200
#
#  Scenario: Create folder
#    When Create folder from file create_folders.json
#    Then Response status should be 201
#
#    Scenario: Update folder
#      When Create folder from file create_folders.json
#      Then Response status should be 200
#      And User store "id" from body as "id"
#      And Update folder with id "id"
#
#  @manual
#  Scenario: not ready
#    When Create folder from files create_folders.json
