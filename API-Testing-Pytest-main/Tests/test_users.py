
import json
from dotenv import load_dotenv
import os

from helpers.session import Session

load_dotenv()

base_url = os.getenv('BASE_URL')
session = Session(base_url=base_url)

def test_fetch_user() :
    path = '/user'
    response = session.request('GET', path)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    id = response.json()['user']['id']
    assert (id != 'undefined' )

