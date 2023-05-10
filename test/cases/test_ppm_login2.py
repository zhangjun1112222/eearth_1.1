import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestLogin:
    """
    登录/登出
    """

    @pytest.mark.parametrize("username,password,assert1,assert2", data['用户登录数据'])
    def test_login(self, username, password, assert1, assert2):
        """
        登陆
        """
        u = ServerInfo.get_url1('/tenant/user/login')
        # print(u)
        # print(data)
        h = {"username": username, "password": password}
        res = requests.post(url=u, json=h)
        assert res.status_code == assert1
        assert res.json()['code'] == assert2

    def test_logout(self, test_login1):
        u = ServerInfo.get_url1('/tenant/user/logout')
        h = {'X-Token': test_login1}
        res = requests.post(url=u, headers=h)
        print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

