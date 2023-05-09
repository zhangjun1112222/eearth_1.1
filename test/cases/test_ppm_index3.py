import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestIndex:
    """
    1.1首页接口
    """
    def test_user_info(self, test_login1):
        """
        用户信息
        """
        u = ServerInfo.get_url1('/tenant/user/info')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_class_list(self, test_login1):
        """
        项目类列表
        """
        u = ServerInfo.get_url1('/tenant/project/class/list')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data'][0]['id']

    def test_class_project_list(self, test_login1):
        """
        类下面的项目
        """
        a = self.test_class_list(test_login1)
        u = ServerInfo.get_url2('/tenant/project/list')
        h = {'X-TOKEN': test_login1}
        d = {'class_id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200


