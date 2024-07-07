import os
import pytest
import json
import requests
from dotenv import load_dotenv
from pytest_steps import test_steps

from helpers.session import Session
from methods.goals_steps import create_goal, get_goals, get_goal, update_goal, delete_goal

# Load environment variables from .env file
load_dotenv()

# Load base URL, team ID, and token from environment
base_url = os.getenv('BASE_URL')
team_id = os.getenv('TEAM_ID')
token = os.getenv('API_TOKEN')

# Initialize session with base URL and token
session = Session(base_url=base_url, token=token)

# Headers for JSON content type
header_app_json = {
    'Content-Type': 'application/json',
}

@pytest.fixture
def create_goal_data():
    """
    Fixture to load data for creating a test goal from a JSON file.
    """
    with open('Test Data/create_goal.json', 'r') as file:
        goal_data = json.load(file)
    return goal_data

@pytest.fixture
def update_goal_data(request):
    """
    Fixture to load data for updating a test goal from a JSON file.
    """
    with open('Test Data/update_goal.json', 'r') as file:
        update_goal_data = json.load(file)

    # Update name and description specifically for the test
    update_goal_data["name"] = request.param["name"]
    update_goal_data["description"] = request.param["description"]

    return update_goal_data

@pytest.fixture
def create_key_result_data():
    """
    Fixture to load data for creating a test key result from a JSON file.
    """
    with open('Test Data/create_key_result.json', 'r') as file:
        key_result_data = json.load(file)
    return key_result_data

@pytest.fixture
def edit_key_result_data():
    """
    Fixture to load data for editing a test key result from a JSON file.
    """
    with open('Test Data/edit_key_result.json', 'r') as file:
        edit_key_result_data = json.load(file)
    return edit_key_result_data

@pytest.fixture
def delete_key_result_data():
    """
    Fixture to load data for deleting a test key result.
    """
    with open('Test Data/delete_key_result.json', 'r') as file:
        delete_key_result_data = json.load(file)
    return delete_key_result_data

@pytest.fixture
def create_goal_next():
    """
    Fixture to create a new goal before creating key results.
    """
    url = f'{base_url}/api/v2/goal'
    payload = {
        "name": "New Goal Name",
        "due_date": "2024-12-31",
        "owner_ids": [183],
        "description": "Description of the goal"
    }
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200, f"Failed to create goal. Status code: {response.status_code}"
    response_json = response.json()
    return response_json['id']

def create_key_result(goal_id, key_result_data):
    """
    Function to create a key result for a specific goal.
    """
    url = f'{base_url}/api/v2/goal/{goal_id}/key_result'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(key_result_data))
    assert response.status_code == 200, f"Failed to create key result. Status code: {response.status_code}"

    response_json = response.json()
    return response_json['key_result_id']

def edit_key_result(key_result_id, edit_key_result_data):
    """
    Function to edit a key result by its identifier.
    """
    url = f'{base_url}/api/v2/key_result/{key_result_id}'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.put(url, headers=headers, data=json.dumps(edit_key_result_data))
    assert response.status_code == 200, f"Failed to edit key result. Status code: {response.status_code}"

    response_json = response.json()
    assert response_json['steps_current'] == edit_key_result_data['steps_current'], "Steps current should be updated"
    assert response_json['note'] == edit_key_result_data['note'], "Note should be updated"

def delete_key_result(key_result_id):
    """
    Function to delete a key result by its identifier.
    """
    url = f'{base_url}/api/v2/key_result/{key_result_id}'
    headers = {
        'Authorization': token
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200, f"Failed to delete key result. Status code: {response.status_code}"

@test_steps('Get goals', 'Create goal', 'Get goal', 'Update goal', 'Delete goal', 'Create goal next', 'Create key results', 'Edit key results', 'Delete key results')
@pytest.mark.parametrize('team_id, expected_status_code, update_goal_data',
                         [(team_id, 200, {"name": "Updated Goal Name", "description": "Updated Goal Description"}),
                          ('', 400, {"name": "Updated Goal Name", "description": "Updated Goal Description"}),
                          ('o87378127812', 400,
                           {"name": "Updated Goal Name", "description": "Updated Goal Description"})],
                         indirect=['update_goal_data'])
def test_goals_lifecycle(team_id, expected_status_code, create_goal_data, update_goal_data, create_key_result_data, create_goal_next, edit_key_result_data):
    """
    Test case to verify the lifecycle of goals and key results:
    1. Get goals from the API.
    2. Create a new goal.
    3. Retrieve the created goal.
    4. Update the created goal.
    5. Delete the updated goal.
    6. Create a new goal before creating key results.
    7. Create key results for the new goal.
    8. Edit the key results.
    9. Delete the key results.
    """
    created_goal_id = None
    key_result_id = None

    try:
        # Step 1: Get goals
        get_goals_response = get_goals(session, team_id)
        assert get_goals_response.status_code == expected_status_code, f"Failed to get goals. Status code: {get_goals_response.status_code}"
        yield

        # Step 2: Create goal
        post_goal_response = create_goal(session, create_goal_data)
        assert post_goal_response.status_code == 200, f"Failed to create goal. Status code: {post_goal_response.status_code}"
        created_goal_id = post_goal_response.json().get('id')
        yield

        # Step 3: Get created goal
        get_goal_response = get_goal(session, created_goal_id)
        assert get_goal_response.status_code == 200, f"Failed to get created goal. Status code: {get_goal_response.status_code}"
        yield

        # Step 4: Update goal
        put_goal_response = update_goal(session, created_goal_id, update_goal_data)
        assert put_goal_response.status_code == 200, f"Failed to update goal. Status code: {put_goal_response.status_code}"
        yield

        # Step 5: Delete goal
        delete_response = delete_goal(session, created_goal_id)
        if delete_response.status_code != 200:
            print(f"Failed to delete goal {created_goal_id}. Status code: {delete_response.status_code}")
        yield

        # Step 6: Create a new goal before creating key result
        new_goal_id = create_goal_next
        yield

        # Step 7: Create key result
        key_result_id = create_key_result(new_goal_id, create_key_result_data)
        yield

        # Step 8: Edit key result
        edit_key_result(key_result_id, edit_key_result_data)
        yield

    finally:
        # Step 9: Delete key result
        if key_result_id:
            delete_key_result(key_result_id)
