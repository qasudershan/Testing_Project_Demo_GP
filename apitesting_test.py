import pytest
import requests


def test_get_status_code_equals_200_negative():
    response = requests.get('https://gorest.co.in/public/v1/users')
    assert response.status_code == 300,"Failed, Expected response code 300 has not found"

def test_get_status_code_equals_200_positive():
    response = requests.get("https://gorest.co.in/public/v1/users")
    assert response.status_code == 200,"Failed, Expected response code 200 not found"

def test_get_check_content_type_is_json():
    response = requests.get("https://gorest.co.in/public/v1/users")
    assert str(response.headers["Content-Type"]).split(";",1)[0] == "application/json","Failed, Expected value not found in response"

def test_get_id():
    response = requests.get("https://gorest.co.in/public/v1/users")
    response_json = response.json()
    assert response_json["data"][0]["id"] == 28109,"Failed, Expected id not found in response"