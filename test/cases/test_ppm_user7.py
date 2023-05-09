import random

import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestUser:
    """
    用户管理
    """
    def test_user_add(self, test_login1):
        """
        角色新增
        """
        b = random.randint(100000, 999999)
        c = str(b)
        u = ServerInfo.get_url1('/tenant/user')
        h = {'X-TOKEN': test_login1}
        d = {'username': c, 'password': '554b4e7dcedaaa04a416ef03a48ace98'}
        res = requests.post(url=u, headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_add1(self, test_login1):
        self.test_user_add(test_login1)

    def test_user_list(self, test_login1):
        """
        用户列表
        """
        u = ServerInfo.get_url1('/tenant/user/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_user_update(self, test_login1):
        """
        用户编辑
        """
        a = self.test_user_list(test_login1)
        b = random.randint(100000, 999999)
        c = str(b)
        u = ServerInfo.get_url1(f'/tenant/user/{a}')
        h = {'X-TOKEN': test_login1}
        d = {'username': c}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_delete(self, test_login1):
        """
        用户删除
        """
        a = self.test_user_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_role_list(self, test_login1):
        """
        角色列表
        """
        u = ServerInfo.get_url1('/tenant/role/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_user_role_add(self, test_login1):
        """
        用户新增角色
        """
        a = self.test_user_list(test_login1)
        b = self.test_role_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/role')
        h = {'X-TOKEN': test_login1}
        d = {"user_id": a, "role_id": b}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_role_list(self, test_login1):
        """
        用户已用的角色列表
        """
        a = self.test_user_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/role/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_user_role_delete(self, test_login1):
        """
        用户角色删除
        """
        a = self.test_user_role_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/role/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_role_add1(self, test_login1):
        self.test_user_role_add(test_login1)

    def test_user_query(self, test_login1):
        """
        用户查询
        """
        u = ServerInfo.get_url1('/tenant/user/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'key': '用户'}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
