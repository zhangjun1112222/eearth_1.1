import pytest
import requests
import yaml
from config.config import ServerInfo


class TestWarning():
    '''
     预警管理
    '''
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_factor(self):
        '''
        预警因子获取：设备，价值，履约
        :return:
        '''
        u=ServerInfo.get_url('/warning/factor/category')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200


    def test_factoring(self):
        '''
        预警触发因子获取
        :return:
        '''
        u=ServerInfo.get_url('/warning/factor/page/1/size/20')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['list'][0]['id']

    def test_rule_add(self):
        '''
        预警规则-添加
        :return:
        '''
        u=ServerInfo.get_url('/warning/rule')
        d={
              "category": "device",
              "id": "string",
              "items": [
                          {
                            "factor_id": "d51ec380331411ed89fe0242ac190002",
                            "next_condition": "",
                            "next_detail_id": "",
                            "operator": "大于",
                            "value": "100"
                          }
                        ],
              "name": "test_warning",
              "remark": "接口创建"
            }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['name']=='test_warning'
        return res.json()['data']['id']


    def test_rule_pagesize(self):
        '''
        预警规则-分页获取
        :return:
        '''
        u=ServerInfo.get_url('/warning/rule/page/1/size/30')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['list'][0]['id']


    def test_rule_detail(self):
        '''
        预警规则-详情
        :return:
        '''
        A=self.test_rule_pagesize()
        u=ServerInfo.get_url('/warning/rule/detail/'+A)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['data']['id']==A




    def test_rule_updata(self):
        '''
        预警规则-修改
        :return:
        '''
        A=self.test_rule_pagesize()
        u=ServerInfo.get_url('/warning/rule/'+A)
        d={
              "category": "fulfillment",
              "id": "string",
              "items": [
                          {
                            "factor_id": "d51eda36331411ed89fe0242ac190002",
                            "next_condition": "",
                            "next_detail_id": "",
                            "operator": "大于",
                            "value": "10"
                          }
                        ],
              "name": "test_001",
              "remark": "接口修改"
           }
        res=requests.put(url=u,json=d)
        print(res.json())
        assert res.status_code==200
        assert res.json()['data']['name']=='test_001'


    def test_rule_delete(self):
        '''
        预警规则-删除
        :return:
        '''
        A=self.test_rule_add()
        u=ServerInfo.get_url('/warning/rule/'+A)
        res=requests.delete(url=u)
        assert res.status_code==200
        assert res.json()['data']==A

