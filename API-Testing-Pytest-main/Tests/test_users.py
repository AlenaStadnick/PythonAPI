
import json
from dotenv import load_dotenv
import os

from helpers.session import Session

load_dotenv()

base_url = os.getenv('BASE_URL')
session = Session(base_url=base_url)

def test_get_user() :

    path = '/user'
    response = session.request('GET', path)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    id = response.json()['user']['id']
    assert (id != 'undefined' )


def test_create_folder() :

    path = '/space/90151393719/folder'
    headers = {
        'Content-Type': 'application/json',
    }
    with open('TestData/create_folder.json', 'r') as file:
        data = json.load(file)

    # Make the POST request
    response = session.request('post', path, headers=headers, data=json.dumps(data))

    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    id = response.json()['id']
    assert (id != 'undefined' )