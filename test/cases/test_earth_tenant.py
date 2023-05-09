import random

import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_earth.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestTenant:
    """
    租户管理
    """

    def test_tenant_add(self, test_login):
        """
        新增租户
        """
        a = random.randint(100000, 999999)
        c = str(a)
        u = ServerInfo.get_url('/tenant')
        h = {'X-TOKEN': test_login}
        d = {"name": c, "desc": "5", "contact": "4"}
        res = requests.post(url=u,  headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_list(self, test_login):
        """
        租户列表
        """
        u = ServerInfo.get_url('/tenant/page/1/size/10')
        h = {'X-TOKEN': test_login}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_tenant_update(self, test_login):
        """
        租户编辑
        """
        a = self.test_tenant_list(test_login)
        b = random.randint(100000, 999999)
        c = str(b)
        u = ServerInfo.get_url(f'/tenant/{a}')
        h = {'X-TOKEN': test_login}
        d = {"name": c, "id": a, "desc":  "5", "contact": "4"}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_app_list(self, test_login):
        """
        应用列表
        """
        u = ServerInfo.get_url('/app/list')
        h = {'X-TOKEN': test_login}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data'][0]['id'], res.json()['data'][1]['id']

    def test_tenant_app_add(self, test_login):
        """
        租户新增应用(无试用期)
        """
        a = self.test_app_list(test_login)
        b = self.test_tenant_list(test_login)
        u = ServerInfo.get_url('/tenant/app')
        d = {"app_id": a[0], "state": 1, "probation": 2, "tenant_id": b}
        h = {'X-TOKEN': test_login}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_app_add1(self, test_login):
        """
        租户新增应用(有试用期)
        """
        a = self.test_app_list(test_login)
        b = self.test_tenant_list(test_login)
        u = ServerInfo.get_url('/tenant/app')
        d = {"app_id": a[1], "state": 1, "probation": 1, "probation_begin": "2023-05-01", "probation_end": "2023-05-31", "tenant_id": b}
        h = {'X-TOKEN': test_login}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_app_list(self, test_login):
        """
        租户已使用的应用列表
        """
        a = self.test_tenant_list(test_login)
        u = ServerInfo.get_url('/tenant/app/page/1/size/50')
        h = {'X-TOKEN': test_login}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id'], res.json()['data']['list'][0]['app_id'], res.json()['data']['list'][0]['tenant_id']

    def test_tenant_app_update(self, test_login):
        """
        应用编辑
        """
        a = self.test_tenant_app_list(test_login)
        # b = self.test_tenant_list(test_login)
        u = ServerInfo.get_url(f'/tenant/app/probation/{a[0]}')
        h = {'X-TOKEN': test_login}
        d = {"id": a[0], "app_id": a[1], "state": 1, "probation": 2, "tenant_id": a[2]}
        res = requests.put(url=u, headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_resource_ava_list(self, test_login):
        """
        可用资源列表
        """
        a = self.test_tenant_app_list(test_login)
        u = ServerInfo.get_url('/tenant/app/resource/available/list')
        h = {'X-TOKEN': test_login}
        d = {'tenant_id': a[2], 'app_id': a[1]}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_resource_list(self, test_login):
        """
        资源列表
        """
        a = self.test_tenant_app_list(test_login)
        u = ServerInfo.get_url('/tenant/app/resource/list')
        h = {'X-TOKEN': test_login}
        d = {'tenant_id': a[2], 'app_id': a[1]}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_app_delete(self, test_login):
        """
        删除租户应用
        """
        a = self.test_tenant_app_list(test_login)
        u = ServerInfo.get_url(f'/tenant/app/{a[0]}')
        h = {'X-TOKEN': test_login}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_delete(self, test_login):
        """
        删除租户
        """
        a = self.test_tenant_list(test_login)
        u = ServerInfo.get_url(f'/tenant/{a}')
        h = {'X-TOKEN': test_login}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['data'] == a