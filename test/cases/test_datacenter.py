import requests

from config.config import ServerInfo

import pytest


class TestDataCenter():
    """
    数据中心
    """
    def test_aircraft_civil_detail(self):
        '''
            通用飞机管理—详情获取
        '''
        u=ServerInfo.get_url('/data/aircraft/civil/detail/1')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_aircraft_civil_op(self):
        """
        通用飞机管理—详情-运营信息
        """
        u=ServerInfo.get_url('/data/aircraft/civil/detail/1/op')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code'] ==200

    def test_aircraft_civil_property(self):
        """
        通用飞机管理—详情-权限信息
        """
        u=ServerInfo.get_url('/data/aircraft/civil/detail/1/property')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code']==200

    def test_aircraft_civil_value(self):
        """
        通用飞机管理—详情-价值信息
        """
        u=ServerInfo.get_url('/data/aircraft/civil/detail/1/value')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code']==200

    def test_aircraft_civil_warning(self):
        """
        通用飞机管理—详情-预警信息
        """
        u=ServerInfo.get_url('/data/aircraft/civil/detail/1/warning')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code']==200

    def test_aircraft_pagesize(self):
        """
        通用飞机管理分页获取
        """
        u=ServerInfo.get_url('/data/aircraft/civil/page/1/size/10')
        res = requests.get(url=u)
        A=res.json()['data']['total']
        if A<10:
            a=A
        else:
            a=10
        assert res.status_code ==200
        assert len(res.json()['data']['list'])==a


    def test_aircraft_commercial_detail(self):
        '''
        商用飞机—详情获取
        '''
        u=ServerInfo.get_url('/data/aircraft/commercial/detail/2')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_aircraft_commercial_op(self):
        """
        商用飞机管理-详情-运营信息
        """
        u=ServerInfo.get_url('/data/aircraft/commercial/detail/2/op')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code'] ==200

    def test_aircraft_commercial_property(self):
        """
        商用飞机管理-详情-权限信息
        """
        u=ServerInfo.get_url('/data/aircraft/commercial/detail/2/property')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code'] ==200

    def test_aircraft_commercial_value(self):
        """
        商用飞机管理-详情-价值信息
        """
        u=ServerInfo.get_url('/data/aircraft/commercial/detail/2/value')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code']==200

    def test_aircraft_commercial_warning(self):
        """
        商用飞机管理-详情-预警信息
        """
        u=ServerInfo.get_url('/data/aircraft/commercial/detail/2/warning')
        res = requests.get(url=u)
        assert res.status_code ==200
        assert res.json()['code'] ==200


    def test_aircraft_commercial_pagesizi(self):
        """
        商用飞机管理-分页获取
        """
        u=ServerInfo.get_url('/data/aircraft/commercial/page/1/size/30')
        p={'key':1}
        res = requests.get(url=u,params=p)
        A=(res.json()['data']['total'])
        if A<30:
            a=A
        else:
            a=30
        assert res.status_code ==200
        assert len(res.json()['data']['list'])==a



    def test_ship_detail(self):
        '''
         船舶管理分页查询
        '''
        u=ServerInfo.get_url('/data/ship/page/1/size/30')
        res=requests.get(url=u)
        A=res.json()['data']['total']
        if A<30:
            a=A
        else:
            a=30
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a

    def test_ship_detail(self):
        '''
        船舶管理-详情
        '''
        u=ServerInfo.get_url('/data/ship/detail/1')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_ship_detail_op(self):
        '''
         船舶管理-运营信息
        '''
        u=ServerInfo.get_url('/data/ship/detail/1/op')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_ship_detail_property(self):
        '''
        船舶管理-权属信息
        '''

        u=ServerInfo.get_url('/data/ship/detail/1/property')
        res=requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_ship_detail_value(self):
        """
        船舶管理-价值信息
        """
        u=ServerInfo.get_url('/data/ship/detail/1/value')
        res=requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200


    def test_vehicle_commercial_pagesize(self):
        '''
        商用车管理-分页查询
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/page/1/size/10')
        res=requests.get(url=u)
        A=res.json()['data']['total']
        if A<10:
            a=A
        else:
            a=10
        assert res.status_code==200
        assert len(res.json()['data']['list'])==a


    def test_vehicle_commercial_detail(self):
        '''
        商用车管理-详情
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/detail/016388d49d7949718385f354f6c7b766')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['data']['id']=='016388d49d7949718385f354f6c7b766'

    def test_vehicle_commercial_detail_op(self):
        '''
        商用车管理-运营信息
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/detail/016388d49d7949718385f354f6c7b766/op')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_vehicle_commercial_detail_value(self):
        '''
        商务车管理-价值信息
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/detail/016388d49d7949718385f354f6c7b766/value')
        res=requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_vehicle_commercial_detail_property(self):
        '''
        商务车管理-权属信息
        :return:
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/detail/016388d49d7949718385f354f6c7b766/property')
        res=requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_vehicle_commercial_detail_warning(self):
        '''
        商务车管理-预警信息
        :return:
        '''
        u=ServerInfo.get_url('/data/vehicle/commercial/detail/016388d49d7949718385f354f6c7b766/warning')
        res=requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200