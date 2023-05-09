import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestRole:
    """
    角色管理
    """

    @pytest.mark.parametrize("name", data['角色名称'])
    def test_role_add(self, name, test_login1):
        """
        角色新增
        """
        u = ServerInfo.get_url1('/tenant/role')
        h = {'X-TOKEN': test_login1}
        d = {'name': name}
        res = requests.post(url=u, headers=h, json=d)
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

    def test_role_update(self, test_login1):
        """
        角色编辑
        """
        a = self.test_role_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/role/{a}')
        h = {'X-TOKEN': test_login1}
        d = {'name': '角色N'}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_role_delete(self, test_login1):
        """
        角色删除
        """
        a = self.test_role_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/role/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_privilege_list(self, test_login1):
        """
        权限列表
        """
        u = ServerInfo.get_url1('/tenant/privilege/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id'], res.json()['data']['list'][1]['id']

    def test_role_privilege_add(self, test_login1):
        """
        角色新增权限
        """
        a = self.test_role_list(test_login1)
        b = self.test_privilege_list(test_login1)
        u = ServerInfo.get_url1('/tenant/role/privilege/multi')
        h = {'X-TOKEN': test_login1}
        d = {"role_id": a, "privilege_id_list": [b[0], b[1]]}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_role_privilege_list(self, test_login1):
        """
        角色已用权限列表
        """
        a = self.test_role_list(test_login1)
        u = ServerInfo.get_url1('/tenant/role/privilege/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_role_privilege_delete(self, test_login1):
        """
        角色权限删除
        """
        a = self.test_role_privilege_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/role/privilege/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_role_list_query(self, test_login1):
        """
        角色列表搜索
        """
        u = ServerInfo.get_url1('/tenant/role/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'key': '角色'}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200