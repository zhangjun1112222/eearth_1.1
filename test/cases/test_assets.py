import pytest
import requests
import yaml
from config.config import ServerInfo
with open (r'C:\Users\zj_001\Desktop\WXM\data\test_assets.yaml','r',encoding='utf-8') as f:
    data=yaml.safe_load(f)

class  TestAssets():
    def setup(self):
        pass
    def teardown(self):
        pass

    @pytest.mark.parametrize("id,expect1,expect2",data['设备管理详情-获取'])
    def test_get_device_details(self,id,expect1,expect2):
        """
        设备管理详情-获取
        """
        u=ServerInfo.get_url(f'/assets/device/detail/{id}')
        res=requests.get(url=u)
        assert res.status_code==expect1
        assert res.json()['code']==expect2
        print(data['设备管理详情-获取'])


    @pytest.mark.parametrize("id,expect1,expect2", [('96cd96c50b12c10de05013ac0c881b04new', 200, 200),
                                                    ('1111111111', 200, 500), (None, 200,500)])
    def test_get_device_details_op(self, id, expect1, expect2):
        """
        设备管理详情-运营信息
        """
        u = ServerInfo.get_url(f'/assets/device/detail/{id}/op')
        res = requests.get(url=u)
        assert res.status_code == expect1
        assert res.json()['code'] == expect2
    #
    @pytest.mark.parametrize("id,expect1,expect2",data['设备管理详情-权限'])
    def test_get_device_details_property(self, id, expect1, expect2):
        """
        设备管理详情-权属信息
        """
        u = ServerInfo.get_url(f'/assets/device/detail/{id}/property')
        res = requests.get(url=u)
        assert res.status_code == expect1
        assert res.json()['code'] == expect2




    @pytest.mark.parametrize("id,expect1,expect2", data['设备管理详情-价值信息'])
    def test_get_device_details_vaule(self, id, expect1, expect2):
        """
        设备管理详情-价值信息
        """
        u = ServerInfo.get_url(f'/assets/device/detail/{id}/value')
        res = requests.get(url=u)
        assert res.status_code == expect1
        assert res.json()['code'] == expect2
    # @
    # def test_get_device_details_warning(self, id, expect1, expect2):
    #     """
    #     设备管理详情-预警信息
    #     """
    #     u = ServerInfo.get_url(f'/assets/device/detail/{id}/warning')
    #     res = requests.get(url=u)
    #     assert res.status_code == expect1
    #     assert res.json()['code'] == expect2


    def test_get_device_pagesize(self):
        """
        设备管理-分页查询
        """
        u = ServerInfo.get_url('/assets/device/page/1/size/20')
        res = requests.get(url=u)
        A=res.json()['data']['total']
        if A<20:
            a=A
        else:
            a=20
        assert res.status_code == 200
        assert (len(res.json()['data']['list']))==a

    def test_get_device_typelist(self):
        """
        设备类型列表获取
        """
        u = ServerInfo.get_url('/assets/device/type/list')
        res = requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200


    def test_get_device_typetree(self):
        """
        设备类型树获取
        """
        u = ServerInfo.get_url('/assets/device/type/tree')
        res = requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200


    def test_get_device_write(self):
        """
          设备管理-编辑
        """
        u = ServerInfo.get_url('/assets/device/4028c6646bb8dca7016c048a8ba10057new') #默认列表第三条数据
        d={"manager_id": "20220622013529709-F609-E3C85677B","self_mortgage":True}  #资管经理id为 赵祝平
        h={'Content-Type': 'application/json'}
        res = requests.put(url=u,json=d,headers=h)
        # print(res.status_code) #为啥接口返回为400
        assert res.status_code == 200
        print(res.text)
        assert res.json()['data']['data']['self_mortgage']==True
        assert res.json()['data']['data']['resource_manager_name']=='赵祝平'

