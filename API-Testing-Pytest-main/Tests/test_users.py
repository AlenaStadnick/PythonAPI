# import json
# import random
# import string
# import pytest
# from dotenv import load_dotenv
# import os
# from pytest_steps import test_steps
# from helpers.session import Session
# # from folder_steps import create_folder
#
# load_dotenv()
#
# base_url = os.getenv('BASE_URL')
# session = Session(base_url=base_url)
#
# @pytest.fixture
# def create_folder_data():
#     with open('TestData/create_folder.json', 'r') as file:
#         data = json.load(file)
#     # Generate a random string of 10 characters
#     random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#     data['name'] = random_string
#     return data
#
# def test_get_user() :
#     path = '/user'
#     response = session.request('GET', path)
#     responseJson = json.loads(response.text)
#     print(responseJson)
#     assert response.status_code == 200
#     id = response.json()['user']['id']
#     assert (id != 'undefined')
#
# # @test_steps('get folders','create_folder' )
# def test_create_folder(create_folder_data) :
#     # Step Get folders
#     print("get folders")
#     get_folders_path = '/space/90151393719/folder'
#     get_folders_response = session.request('get', get_folders_path)
#     assert get_folders_response.status_code == 200
#     # yield
#
#     print("get folders22")
#     get_folders_path = '/space/90151393719/folder'
#     get_folders_response = session.request('get', get_folders_path)
#     assert get_folders_response.status_code == 200
#     yield
#     # Make the POST request
#     headers = {
#         'Content-Type': 'application/json',
#     }
#
#
#
#
#
#     #
#
#     # # Make the POST request
#     # response = session.request('post', path, headers=headers, data=json.dumps(create_folder_data))
#     #
#     # responseJson = json.loads(response.text)
#     # print(responseJson)
#     # assert response.status_code == 200
#     # id = response.json()['id']
#     # assert (id != 'undefined' )