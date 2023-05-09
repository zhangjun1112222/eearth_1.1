import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestProjectGroup:
    """
    项目组
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
        return res.json()['data']['tenant_id'], res.json()['data']['tenant_name']

    @pytest.mark.parametrize("name", data['项目组名称'])
    def test_project_group_add(self, name, test_login1):
        """
        项目组新增
        """
        a = self.test_user_info(test_login1)
        u = ServerInfo.get_url1('/tenant/project/group')
        h = {'X-TOKEN': test_login1}
        d = {'name': name, 'desc': '描述'}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_project_group_list(self, test_login1):
        """
        项目组列表
        """
        u = ServerInfo.get_url1('/tenant/project/group/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_project_group_update(self, test_login1):
        """
        项目组编辑
        """
        a = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/project/group/{a}')
        h = {'X-TOKEN': test_login1}
        d = {'name': 'N组', 'desc': '描述1'}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_project_group_delete(self, test_login1):
        """
        项目组删除
        """
        a = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/project/group/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_project_list(self, test_login1):
        """
        获取所有项目
        """
        a = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url2('/tenant/project/page/1/size/1000')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_group_add_project(self, test_login1):
        """
        项目组加项目
        """
        a = self.test_project_group_list(test_login1)
        b = self.test_project_list(test_login1)
        u = ServerInfo.get_url1('/tenant/project/group/project')
        h = {'X-TOKEN': test_login1}
        d = {'project_group_id': a, 'project_id': b}
        res = requests.post(url=u, headers=h, json=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_group_project_list(self, test_login1):
        """
        项目组里的已添加的项目列表
        """
        a = self.test_project_group_list(test_login1)
        u = ServerInfo.get_url1('/tenant/project/group/project/page/1/size/10')
        h = {'X-TOKEN': test_login1}
        d = {'id': a}
        res = requests.get(url=u, headers=h, params=d)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][-1]['id']

    def test_group_project_delete(self, test_login1):
        """
        项目组里删除项目
        """
        a = self.test_group_project_list(test_login1)
        u = ServerInfo.get_url1(f'/tenant/project/group/project/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)

    def test_group_add_project1(self, test_login1):
        """
        项目组加项目
        """
        self.test_group_add_project(test_login1)






