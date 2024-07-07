import json


def get_goals(session, team_id):
    """
    Get all goals for a team.

    :param session: Session object to make the request
    :param team_id: ID of the team
    :return: Response JSON from the API
    """
    url = f'/api/v2/team/{team_id}/goal?include_completed=true'
    response = session.request('get', url)
    return response


def create_goal(session, goal_data):
    """
    Create a new goal.

    :param session: Session object to make the request
    :param goal_data: Data for creating the goal
    :return: Response JSON from the API
    """
    url = '/api/v2/goal'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('post', url, headers=headers, json=goal_data)
    return response


def get_goal(session, goal_id):
    """
    Get a specific goal by its ID.

    :param session: Session object to make the request
    :param goal_id: ID of the goal
    :return: Response JSON from the API
    """
    url = f'/api/v2/goal/{goal_id}'
    response = session.request('get', url)
    return response


def update_goal(session, goal_id, update_data):
    """
    Update a goal by its ID.

    :param session: Session object to make the request
    :param goal_id: ID of the goal
    :param update_data: Data for updating the goal
    :return: Response JSON from the API
    """
    url = f'/api/v2/goal/{goal_id}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('put', url, headers=headers, json=update_data)
    return response


def delete_goal(session, goal_id):
    """
    Delete a goal by its ID.

    :param session: Session object to make the request
    :param goal_id: ID of the goal
    :return: Response JSON from the API
    """
    url = f'/api/v2/goal/{goal_id}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('delete', url, headers=headers)
    return response


def create_goal_next(session, goal_data):
    """
    Create a new goal specifically for the next test.

    :param session: Session object to make the request
    :param goal_data: Data for creating the goal
    :return: Goal ID of the newly created goal
    """
    url = '/api/v2/goal'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('post', url, headers=headers, json=goal_data)
    response.raise_for_status()  # Raise an error if the request fails
    response_json = response.json()
    return response_json['id']


def create_key_result(session, goal_id, key_result_data):
    """
    Create a key result for a specific goal.

    :param session: Session object to make the request
    :param goal_id: ID of the goal
    :param key_result_data: Data for creating the key result
    :return: Response JSON from the API
    """
    url = f'/api/v2/goal/{goal_id}/key_result'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('post', url, headers=headers, json=key_result_data)
    return response


def edit_key_result(session, key_result_id, edit_data):
    """
    Edit a key result by its ID.

    :param session: Session object to make the request
    :param key_result_id: ID of the key result
    :param edit_data: Data for editing the key result
    :return: Response JSON from the API
    """
    url = f'/api/v2/key_result/{key_result_id}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('put', url, headers=headers, json=edit_data)
    return response


def delete_key_result(session, key_result_id):
    """
    Delete a key result by its ID.

    :param session: Session object to make the request
    :param key_result_id: ID of the key result
    :return: Response JSON from the API
    """
    url = f'/api/v2/key_result/{key_result_id}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = session.request('delete', url, headers=headers)
    return response
