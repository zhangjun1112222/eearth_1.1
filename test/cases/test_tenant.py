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

    def test_tenant_list(self, test_login):
        """
        租户列表
        """
        u = ServerInfo.get_url('/tenant/page/1/size/10')
        h = {'X-TOKEN': test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_tenant_add(self, test_login):
        """
        新增租户
        """
