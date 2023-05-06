import pytest
import requests
import yaml
from config.config import ServerInfo


with open (r'C:\Users\zj_001\Desktop\WXM\data\test_assets.yaml','r',encoding='utf-8') as f:
    data=yaml.safe_load(f)

class TestExtData():
    '''
    外部数据
    '''
    def test_gip_pagesize(self):
        '''
         普洛斯管理分页获取
        '''
        u=ServerInfo.get_url('/ext-data/glp/page/1/size/10?key=%E6%A0%87%E5%93%8145%E5%B0%BA')
        res=requests.get(url=u)
        A=res.json()['data']['total']
        if A<10:
            a=A
        else:
            a=10
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a

    # def test_gip_detail(self):
    #     '''
    #     普洛斯管理-详情获取
    #     '''
    #     u=ServerInfo.get_url('/ext-data/glp/detail/007d47f3e7c848f1a4e584d294a420e5')
    #     res=requests.get(url=u)
    #     assert res.status_code==200
    #     assert res.json()['code']==200

    def test_gip_detail_op(self):
        '''
        普洛斯详情-运营信息
        '''
        u=ServerInfo.get_url('/ext-data/glp/detail/007d47f3e7c848f1a4e584d294a420e5/op')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_gip_detail_property(self):
        '''
        普洛斯详情—权属信息
        '''
        u=ServerInfo.get_url('/ext-data/glp/detail/007d47f3e7c848f1a4e584d294a420e5/property')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_gip_detail_value(self):
        '''
        普洛斯详情—价值信息
        '''
        u=ServerInfo.get_url('/ext-data/glp/detail/007d47f3e7c848f1a4e584d294a420e5/value')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_gip_detail_warning(self):
        '''
        普洛斯详情—预警信息
        '''
        u=ServerInfo.get_url('/ext-data/glp/detail/007d47f3e7c848f1a4e584d294a420e5/warning')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200


    def test_xiaoju_pagesize(self):
        '''
        小菊管理-分页获取
        :return:
        '''
        u=ServerInfo.get_url('/ext-data/xiaoju/page/1/size/10')
        res=requests.get(url=u)
        A=res.json()['data']['total']
        if A<10:
            a=A
        else:
            a=10
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a

    # def  test_xiaoju_detail(self):
    #     '''
    #     小菊管理-详情获取
    #     :return:
    #     '''
    #     u=ServerInfo.get_url('/ext-data/xiaoju/detail/4028c66479c7af8b0179cb6c2be702be')
    #     res=requests.get(url=u)
    #     assert  res.status_code==200
    #     assert  res.json()['code']==200

    def  test_xiaoju_detail_op(self):
        '''
        小菊管理详情-运营信息
        :return:
        '''
        u=ServerInfo.get_url('/ext-data/xiaoju/detail/4028c66479c7af8b0179cb6c2be702be/op')
        res=requests.get(url=u)
        assert  res.status_code==200
        assert  res.json()['code']==200

    def test_xiaoju_detail_property(self):
            '''
            小菊管理详情-运营信息
            :return:
            '''
            u = ServerInfo.get_url('/ext-data/xiaoju/detail/4028c66479c7af8b0179cb6c2be702be/property')
            res = requests.get(url=u)
            assert res.status_code == 200
            assert res.json()['code'] == 200

    def  test_xiaoju_detail_value(self):
        '''
        小菊管理详情-价值信息
        :return:
        '''
        u=ServerInfo.get_url('/ext-data/xiaoju/detail/4028c66479c7af8b0179cb6c2be702be/value')
        res=requests.get(url=u)
        assert  res.status_code==200
        assert  res.json()['code']==200

    def  test_xiaoju_detail_warning(self):
        '''
        小菊管理详情-预警信息
        :return:
        '''
        u=ServerInfo.get_url('/ext-data/xiaoju/detail/4028c66479c7af8b0179cb6c2be702be/warning')
        res=requests.get(url=u)
        assert  res.status_code==200
        assert  res.json()['code']==200