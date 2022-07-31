
import requests


def test_login():
    login_url = "http://47.92.149.0:9000/login"
    json_data = {
        "phone": "13888888882",
        "password": "123456",
    }
    r = requests.request("POST", url=login_url, json=json_data)
    print(r.json())
    token = r.json().get("data")
    cookie = {"y-token": token}
    r = requests.request("GET", url="http://47.92.149.0:9000/user/detail", cookies=cookie)
    print(r.json())


def test_login_success():
    login_url = "http://47.92.149.0:9000/login"
    json_data = {
        "phone": "13888888882",
        "password": "123456",
    }
    session = requests.Session()
    r = session.request("POST", url=login_url, json=json_data)
    print(r.json())
    r = session.request("GET", url="http://47.92.149.0:9000/user/detail")
    print(r.json())
