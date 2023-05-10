import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
data_period_start = '2023-05-01'
data_period_end = "2023-06-30"

class TestOrder:
    """
    订单管理
    """
    def test_project_list(self, test_login1):
        """
        项目列表
        """
        u = ServerInfo.get_url2('/tenant/project/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_order_periods(self, test_login1):
        """
        订单期数计算
        """
        u = ServerInfo.get_url1('/common/periods-of-daterange')
        h = {'X-TOKEN': test_login1}
        d = {'day': 1, 'end': data_period_end, 'start': data_period_start, 'type': 'week'}
        res = requests.post(url=u, headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']

    def test_order_add(self, test_login1):
        """
        订单申请
        """
        a = self.test_project_list(test_login1)
        b = self.test_order_periods(test_login1)
        u = ServerInfo.get_url2('/tenant/project/order')
        h = {'X-TOKEN': test_login1}
        d = {'data_period': 1, 'data_period_end': data_period_end,  'data_period_start': data_period_start, 'data_period_total': b,  'data_period_type':  "W", 'project_id': a}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_list(self, test_login1):
        """
        订单列表
        """
        u = ServerInfo.get_url2('/tenant/project/order/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_order_update(self, test_login1):
        """
        订单编辑
        """
        a = self.test_order_list(test_login1)
        b = self.test_order_periods(test_login1)
        c = self.test_project_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/update/{a}')
        # print(u)
        h = {'X-TOKEN': test_login1}
        d = {'data_period': 1, 'data_period_end': data_period_end,  'data_period_start': data_period_start, 'data_period_total': b,  'data_period_type':  "W", 'project_id': c}
        res = requests.put(url=u, headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_delete(self, test_login1):
        """
        订单删除未提交
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/delete/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_add1(self, test_login1):
        self.test_order_add(test_login1)

    def test_order_commit(self, test_login1):
        """
        订单提交
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/commit/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_recommit(self, test_login1):
        """
        订单重复提交（已提交状态再次提交）
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/commit/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 8201

    def test_order_commit_delete(self, test_login1):
        """
        删除已提交订单
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/delete/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 8201

    def test_order_cancel(self, test_login1):
        """
        订单取消
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/cancel/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_cancel1(self, test_login1):
        """
        订单取消（订单未提交）
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/order/cancel/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.put(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 8201

    def test_order_commit1(self, test_login1):
        self.test_order_commit(test_login1)

    def test_order_refuse(self, test_login, test_login1):
        """
        审核拒绝(没写拒绝理由)
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url(f'/tenant/app/project/order/{a}/refuse')
        h = {'X-TOKEN': test_login}
        d = {"id": a, "refuse_reason": None}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 8213

    def test_order_refuse1(self, test_login, test_login1):
        """
        审核拒绝
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url(f'/tenant/app/project/order/{a}/refuse')
        h = {'X-TOKEN': test_login}
        d = {"id": a, "refuse_reason": '拒绝不需要原因'}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_update1(self, test_login1):
        self.test_order_update(test_login1)

    def test_order_commit2(self, test_login1):
        self.test_order_commit(test_login1)

    def test_order_accept(self, test_login, test_login1):
        """
        审核通过
        """
        a = self.test_order_list(test_login1)
        u = ServerInfo.get_url(f'/tenant/app/project/order/{a}/accept')
        h = {'X-TOKEN': test_login}
        d = {'id': a}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_order_query(self, test_login1):
        """
        订单搜索
        """
        a = self.test_project_list(test_login1)
        u = ServerInfo.get_url2('/tenant/project/order/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_earth_tenant_list(self, test_login):
        """
        租户列表
        """
        u = ServerInfo.get_url('/tenant/list')
        h = {'X-TOKEN': test_login}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data'][0]['id']

    def test_earth_tenant_project_list(self, test_login):
        """
        租户对应的项目
        """
        a = self.test_earth_tenant_list(test_login)
        u = ServerInfo.get_url('/project/list')
        h = {'X-TOKEN': test_login}
        d = {'tenant_id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data'][0]['id']

    def test_earth_order_query(self, test_login):
        """
        地球云订单查询
        # """
        a = self.test_earth_tenant_list(test_login)
        b = self.test_earth_tenant_project_list(test_login)
        u = ServerInfo.get_url('/tenant/app/project/order/page/1/size/10')
        h = {'X-TOKEN': test_login}
        d = {'page': 1, 'size': 10, 'key':  '测试', 'tenant_id': a, 'project_id': b, 'apply_state': 3}
        res = requests.get(url=u, headers=h, params=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200