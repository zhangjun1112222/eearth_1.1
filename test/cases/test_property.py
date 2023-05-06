import pytest
import requests
import yaml
from config.config import ServerInfo

class TestProperty():
    '''
    权属管理
    '''
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_contract_pagesize(self):
        '''
        合同管理—分页查询
        :return:
        '''
        u=ServerInfo.get_url('/property/contract/page/1/size/10?key=%E7%94%B5')
        res=requests.get(url=u)
        # print(res.json()['data']['total'])
        A=res.json()['data']['total']
        if A<10:
            a=A
        else:
            a=10
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a


    def test_contract_detail(self):
        '''
        合同详情获取
        :return:
        '''
        u=ServerInfo.get_url('/property/contract/detail/ZHZL(22)10ZL015')
        res=requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['data']['id']=='ZHZL(22)10ZL015'

    def test_contract_lease_pagesize(self):
        '''
        租赁合同管理_分页获取
        :return:
        '''
        u=ServerInfo.get_url('/property/contract/lease/page/1/size/10')
        res=requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code']==200


    def test_customer_pagesize(self):
        '''
        客户管理-分页查询
        :return:
        '''
        u=ServerInfo.get_url('/property/customer/page/1/size/30?key=%E9%87%8D%E5%BA%86')
        res=requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a


    def test_customer_detail(self):
        '''
        客户详情获取
        :return:
        '''
        u=ServerInfo.get_url('/property/customer/detail/4028c6646bb8e336016be106a4d80986')
        res=requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['data']['name']=="重庆长寿开发投资(集团)有限公司"


    def test_insurance_pagesize(self):
        '''
        保险管理-分页查询
        :return:
        '''
        u=ServerInfo.get_url('/property/insurance/page/1/size/30?key=%E7%94%B5')
        res=requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a

    def test_insurance_detail(self):
        '''
        保险管理详情
        :return:
        '''
        u=ServerInfo.get_url('/property/insurance/detail/2022-03-14-01-DA29774F1150DC37E050A8C07ABE3439')
        res=requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['data']['contract_no']=="ZHZL(19)02HZ045"