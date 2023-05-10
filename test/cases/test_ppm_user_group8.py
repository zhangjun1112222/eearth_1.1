import random

import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestUserGroup:
    """
    用户组管理
    """

    @pytest.mark.parametrize("name", data['用户组名称'])
    def test_user_group_add(self, name, test_login1):
        """
        用户组新增
        """
        u = ServerInfo.get_url1('/tenant/user/group')
        h = {'X-TOKEN': test_login1}
        d = {'name': name}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_group_list(self, test_login1):
        """
        用户组列表
        """
        u = ServerInfo.get_url1('/tenant/user/group/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_user_group_update(self, test_login1):
        """
        用户组编辑
        """
        a = self.test_user_group_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/group/{a}')
        h = {'X-TOKEN': test_login1}
        d = {'name': '用户组N'}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_group_delete(self, test_login1):
        """
        用户组删除
        """
        a = self.test_user_group_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/group/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_user_list(self, test_login1):
        """
        用户列表
        """
        u = ServerInfo.get_url1('/tenant/user/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_group_user_add(self, test_login1):
        """
        用户组添加用户
        """
        a = self.test_user_group_list(test_login1)
        b = self.test_user_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/user')
        h = {'X-TOKEN': test_login1}
        d = {"user_group_id": a, "user_id": b}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_group_user_readd(self, test_login1):
        """
        用户组重复添加用户
        """
        a = self.test_user_group_list(test_login1)
        b = self.test_user_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/user')
        h = {'X-TOKEN': test_login1}
        d = {"user_group_id": a, "user_id": b}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 511

    def test_group_user_list(self, test_login1):
        """
        用户组用户列表
        """
        a = self.test_user_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/user/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_group_user_delete(self, test_login1):
        """
        用户组里用户删除
        """
        a = self.test_group_user_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/group/user/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_group_user_add1(self, test_login1):
        """
        用户组里重新添加一个用户
        """
        self.test_group_user_add(test_login1)

    def test_project_group_list(self, test_login1):
        """
        项目组列表
        """
        a = self.test_user_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/project/group/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_group_project_group_add(self, test_login1):
        """
        项目组添加
        """
        a = self.test_user_group_list(test_login1)
        b = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/project/group')
        h = {'X-TOKEN': test_login1}
        d = {"user_group_id": a, "project_group_id": b}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_group_project_group_readd(self, test_login1):
        """
        项目组重复添加
        """
        a = self.test_user_group_list(test_login1)
        b = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/project/group')
        h = {'X-TOKEN': test_login1}
        d = {"user_group_id": a, "project_group_id": b}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 511

    def test_group_project_group_list(self, test_login1):
        """
        用户组里项目组列表
        """
        a = self.test_user_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/user/group/project/group/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_group_project_group_delete(self, test_login1):
        """
        用户组里删除项目组
        """
        a = self.test_group_project_group_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/user/group/project/group/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_group_project_group_add1(self, test_login1):
        """
        重新添加一个项目组
        """
        self.test_group_project_group_add(test_login1)

    def test_user_group_query(self, test_login1):
        """
        用户组查询
        """
        u = ServerInfo.get_url1('/tenant/user/group/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'key': '组'}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200








