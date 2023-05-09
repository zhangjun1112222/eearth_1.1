import pytest
import yaml
from config.config import ServerInfo
import requests
from test.cases import data_path
with open(f'{data_path}/test_1.1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

class TestProject:
    """
    v1.1项目
    """
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
        return res.json()['data'][-1]['id']

    @pytest.mark.parametrize("name", data['项目名称'])
    def test_project_add(self, name, test_login1):
        """
        新增项目
        """
        a = self.test_class_list(test_login1)
        u = ServerInfo.get_url2('/tenant/project')
        h = {'X-TOKEN': test_login1}
        d = {"name": name, "class_id": a, "type_code":"PV","lng":"1","lat":"1","desc":"描述","position":"{\"type\":\"FeatureCollection\",\"name\":\"项目范围\",\"crs\":{\"type\":\"name\",\"properties\":{\"name\":\"urn:ogc:def:crs:OGC:1.3:CRS84\"}},\"features\":[{\"type\":\"Feature\",\"properties\":{\"id\":null},\"geometry\":{\"type\":\"MultiPolygon\",\"coordinates\":[[[[116.08180825847542,39.65233983150817],[116.09506631229354,39.65233983150817],[116.09506631229354,39.6453330441588],[116.08180825847542,39.6453330441588]]]]}}]}","position_type":"rectangle","associated_list":[{"name":"关联地块","position_type":"rectangle","position":"{\"type\":\"FeatureCollection\",\"name\":\"项目范围\",\"crs\":{\"type\":\"name\",\"properties\":{\"name\":\"urn:ogc:def:crs:OGC:1.3:CRS84\"}},\"features\":[{\"type\":\"Feature\",\"properties\":{\"id\":null},\"geometry\":{\"type\":\"MultiPolygon\",\"coordinates\":[[[[116.08021673112611,39.647576500890345],[116.08307416674259,39.647576500890345],[116.08307416674259,39.645737512979196],[116.08021673112611,39.645737512979196]]]]}}]}"}]}
        res = requests.post(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_project_list(self, test_login1):
        """
        项目列表
        """
        u = ServerInfo.get_url2('/tenant/project/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        res = requests.get(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        return res.json()['data']['list'][0]['id']

    def test_project_update(self, test_login1):
        """
        项目编辑
        """
        a = self.test_project_list(test_login1)
        b = self.test_class_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/{a}')
        h = {'X-TOKEN': test_login1}
        d = {"name": '大石坝2', "class_id": b, "type_code":"PV","lng":"1","lat":"1","desc":"描述","position":"{\"type\":\"FeatureCollection\",\"name\":\"项目范围\",\"crs\":{\"type\":\"name\",\"properties\":{\"name\":\"urn:ogc:def:crs:OGC:1.3:CRS84\"}},\"features\":[{\"type\":\"Feature\",\"properties\":{\"id\":null},\"geometry\":{\"type\":\"MultiPolygon\",\"coordinates\":[[[[116.08180825847542,39.65233983150817],[116.09506631229354,39.65233983150817],[116.09506631229354,39.6453330441588],[116.08180825847542,39.6453330441588]]]]}}]}","position_type":"rectangle","associated_list":[{"name":"关联地块","position_type":"rectangle","position":"{\"type\":\"FeatureCollection\",\"name\":\"项目范围\",\"crs\":{\"type\":\"name\",\"properties\":{\"name\":\"urn:ogc:def:crs:OGC:1.3:CRS84\"}},\"features\":[{\"type\":\"Feature\",\"properties\":{\"id\":null},\"geometry\":{\"type\":\"MultiPolygon\",\"coordinates\":[[[[116.08021673112611,39.647576500890345],[116.08307416674259,39.647576500890345],[116.08307416674259,39.645737512979196],[116.08021673112611,39.645737512979196]]]]}}]}"}]}
        res = requests.put(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_project_delete(self, test_login1):
        """
        项目删除
        """
        a = self.test_project_list(test_login1)
        u = ServerInfo.get_url2(f'/tenant/project/{a}')
        h = {'X-TOKEN': test_login1}
        res = requests.delete(url=u, headers=h)
        assert res.status_code == 200
        assert res.json()['code'] == 200

