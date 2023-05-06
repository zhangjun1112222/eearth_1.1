import pytest
import requests
import yaml
from config.config import ServerInfo

class TestValue():
    '''
    价值管理
    '''
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_ruleadd(self):
        '''
        价值规则-添加
        :return:
        '''
        u=ServerInfo.get_url('/value/rule')
        d={
            "day_by": 1,
            "id": "string",
            "month": 10,
            "name": "test_test",
            "period_list": [
                 {
                    "end_at": 5,
                    "growth_rate": 10,
                    "start_at": 1
                }
                            ],
            "salvage_rate": 0,
            "trigger_by": 0,
            "type": 1,
            "value_from": "1"
                }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['id']


    def test_ruleupdate(self):
        '''
        价值规则-编辑
        :return:
        '''
        A=self.test_ruleadd()
        d = {
            "day_by": 2,
            "id": "string",
            "month": 10,
            "name": "testandtest",
            "period_list": [
                {
                    "end_at": 5,
                    "growth_rate": 10,
                    "start_at": 1
                }
            ],
            "salvage_rate": 10,
            "trigger_by": 0,
            "type": 2,
            "value_from": "2"
                }
        u=ServerInfo.get_url('/value/rule/'+A)
        # print(u)
        res=requests.put(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['name']=='testandtest'

    def test_ruledelete(self):
        '''
        价值规则-删除
        :return:
        '''
        A=self.test_ruleadd()
        u=ServerInfo.get_url('/value/rule/'+A)
        res=requests.delete(url=u)
        assert res.status_code==200
        assert res.json()['data']==A


    def test_rule_basicdata(self):
        '''
        基础数据获取
        :return:
        '''
        u=ServerInfo.get_url('/value/rule/basic-data')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_rule_detail(self):
        '''
        价值规则-详情
        :return:
        '''
        A=self.test_rulepagesize()
        a=A[0]
        print(a)
        u=ServerInfo.get_url('/value/rule/detail/'+a)
        print(u)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_rule_simulate(self):
        '''
        价值规则模拟
        :return:
        '''
        u=ServerInfo.get_url('/value/rule/simulate?num=100')
        d={
            "day_by": 1,
            "id": "string",
            "month": 0,
            "name": "",
            "period_list": [
                            {
                                "end_at": 3,
                                "growth_rate": 10,
                                "start_at": 1
                            }
                            ],
            "salvage_rate": 0,
            "trigger_by": 0,
            "type": 1,
            "value_from": "1"
            }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['Items'][2]['value']==120

    def test_rulepagesize(self):
        '''
        价值规则分页查询
        :return:
        '''
        u=ServerInfo.get_url('/value/rule/page/1/size/30')
        res=requests.get(url=u)
        A=res.json()['data']['total']
        if A<30:
            a=A
        else:
            a=30
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a
        return res.json()['data']['list'][0]['id'],res.json()['data']['list'][1]['id']



    def test_sceneadd(self):
        '''
        价值场景-添加
        :return:
        '''
        A=self.test_scene_rulelist()
        print(A)
        u=ServerInfo.get_url('/value/scene')
        d={
              "id": "",
              "item_list": [
                           {
                              "target": "96cd96c50f32c10de05013ac0c881b04",
                              "target_name": "",
                              "type": "asset_id",
                              "type_name": "具体资产"
                           }
                            ],
              "name": "test_scene",
              "priority": 3,
              "remark": "场景的备注",
              "valuation_rule_d_id": A[1],
              "valuation_rule_d_name": "",
              "valuation_rule_e_id": A[0],
              "valuation_rule_e_name": ""
        }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['code']==200
        # print(res.json()['data']['id'])
        return res.json()['data']['id']

    def test_scene_updata(self):
        '''
        价值场景-编辑
        :return:
        '''
        A=self.test_scene_pagesize()
        B=self.test_scene_rulelist()
        print(A)
        u=ServerInfo.get_url('/value/scene/'+A)
        # print(u)
        d = {
            "id": A,
            "item_list": [
                {
                    "target": "4028c6646a2bcd49016a9dbb880b0042",
                    "target_name": "制药生产线",
                    "type": "asset_id",
                    "type_name": "具体资产"
                }
            ],
            "name": "scene_updata",
            "priority": 3,
            "remark": "场景的备注1",
            "valuation_rule_d_id": B[1],
            "valuation_rule_d_name": "",
            "valuation_rule_e_id": B[0],
            "valuation_rule_e_name": ""
        }
        res=requests.put(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['name']=='scene_updata'



    def test_scene_pagesize(self):
        '''
        价值场景-分页查询
        :return:
        '''
        u=ServerInfo.get_url('/value/scene/page/1/size/30')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['list'][0]['id']
        # a=res.json()['data']['list'][0]['id']
        # print(a)


    def test_scene_delete(self):
        '''
        价值场景-删除
        :return:
        '''
        A=self.test_sceneadd()
        u=ServerInfo.get_url('/value/scene/'+A)
        # print(u)
        res=requests.delete(url=u)
        assert res.status_code==200
        assert res.json()['data']==A


    def test_scene_basic_data(self):
        '''
        价值场景-基础数据获取
        :return:
        '''
        u=ServerInfo.get_url('/value/scene/basic-data')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200


    # def test_scene_search(self):
    #     '''
    #     价值场景目标值搜素
    #     :return:
    #     '''

    def test_scene_detail(self):
        '''
        价值场景-详情
        :return:
        '''
        A=self.test_scene_pagesize()
        u=ServerInfo.get_url('/value/scene/detail/'+A)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['data']['id']==A


    def test_scene_rulelist(self):
        '''
        价值场景新增时的规则列表
        :return:
        '''
        u=ServerInfo.get_url('/value/scene/rule/list')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data'][0]['item_list'][0]['key'],res.json()['data'][1]['item_list'][0]['key']

    # def test_scene_simulate(self):
    #     '''
    #     价值场景-场景模拟
    #     :return:
    #     '''