import pytest
import requests


from config.config import ServerInfo

@pytest.fixture(scope='function')
def test_login():  # 数字地球云管理员登陆
    u = ServerInfo.get_url('/sys/user/login')
    d = {'username': 'admin', 'password': 'e10adc3949ba59abbe56e057f20f883e', "rememberMe": "false"}
    # 账号：admin 密码：123456

    res = requests.post(url=u, json=d)
    # print(res.json())
    return res.json()['data']['token']


@pytest.fixture(scope='function')
def test_login1():   #1.1’管理员‘登陆
    u = ServerInfo.get_url1('/tenant/user/login')
    d = {'username': '管理员', 'password': 'e10adc3949ba59abbe56e057f20f883e', "rememberMe": "false"}
    # 账号：管理员 密码：123456

    res = requests.post(url=u, json=d)
    # print(res.json())
    return res.json()['data']['token']
