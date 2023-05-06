import pytest
import requests
import yaml
from config.config import ServerInfo

class TestSystem():
    '''
    系统管理
    '''
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_userpagesize(self):
        '''
        用户分页
        :return:
        '''
        u=ServerInfo.get_url('/sys/user/page/1/size/10?key=%E7%AB%B9%E4%BA%91')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 10:
            a = A
        else:
            a = 10
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a

    def test_rolepagesize(self):
            '''
            角色分页
            :return:
            '''
            u = ServerInfo.get_url('/sys/role/page/1/size/10')
            res = requests.get(url=u)
            A = res.json()['data']['total']
            if A < 10:
                a = A
            else:
                a = 10
            assert res.status_code == 200
            assert len(res.json()['data']['list']) == a

    def test_postpagesize(self):
        '''
        岗位分页
        :return:
        '''
        u=ServerInfo.get_url('/sys/post/page/1/size/30?key=%E8%B5%84%E7%AE%A1')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 10:
            a = A
        else:
            a = 10
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a


    def test_deptpagesize(self):
        '''
        部门分页
        :return:
        '''
        u=ServerInfo.get_url('/sys/dept/page/1/size/30?key=%E6%80%BB%E9%83%A8')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a

    def test_logpagesize(self):
        '''
        日志分页
        :return:
        '''
        u = ServerInfo.get_url('/sys/op-log/page/1/size/30?operator=t&start=1665417600&end=1665504000')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a

    def test_dictadd(self):
        '''
        字典添加
        :return:
        '''
        u=ServerInfo.get_url('/sys/dict')
        d={"description": "test001","name": "test001"}
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['id']

    def test_dictpagesize(self):
        '''
        字典分页查询
        :return:
        '''
        u = ServerInfo.get_url('/sys/dict/page/1/size/30?key=test001')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a

    def test_dictpagesize1(self):
        '''
        字典分页查询
        :return:
        '''
        u = ServerInfo.get_url('/sys/dict/page/1/size/30')
        res = requests.get(url=u)
        A = res.json()['data']['total']
        if A < 30:
            a = A
        else:
            a = 30
        assert res.status_code == 200
        assert len(res.json()['data']['list']) == a
        return res.json()['data']['list'][0]['id']

    def test_dictupdate(self):
        '''
        字典更新
        :return:
        '''
        A = self.test_dictpagesize1()
        u=ServerInfo.get_url('/sys/dict/'+A)
        d={"description": "test002","name": "test002"}
        res=requests.put(url=u,json=d)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_dictdelete(self):
        '''
        字典删除
        :return:
        '''
        A=self.test_dictadd()
        u=ServerInfo.get_url('/sys/dict/'+A)
        res=requests.delete(url=u)
        assert res.status_code==200
        assert res.json()['code']==200


    def test_dictdetail(self):
        '''
        字典详情
        :return:
        '''
        A=self.test_dictpagesize1()
        u=ServerInfo.get_url('/sys/dict/detail/'+A)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_dictitemlist(self):
        '''
        字典节点列表
        :return:
        '''
        A=self.test_dictpagesize1()
        u=ServerInfo.get_url('/sys/dict/'+A+'/item/list')
        # print(u)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200
        # print(res.json()['data'][0]['id'])
        return res.json()['data'][0]['id']

    def test_dictitemdetail(self):
        '''
        字典节点详情
        :return:
        '''
        A=self.test_dictitemlist()
        u=ServerInfo.get_url('/sys/dict/item/detail/'+A)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_dictitemadd(self):
        '''
        字典节点添加
        :return:
        '''
        A=self.test_dictpagesize1()
        u = ServerInfo.get_url('/sys/dict/' + A + '/item')
        d = {"description": "节点描述","name": "节点名字","order": 1000,"value": "节点值"}
        res=requests.post(url=u,json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200
        # print(res.json()['data']['id'])
        return res.json()['data']['id']

    def test_dictitemupdate(self):
        '''
        字典节点编辑
        :return:
        '''
        A=self.test_dictitemlist()
        u=ServerInfo.get_url('/sys/dict/item/'+A)
        d={"description": "节点的描述111","name": "节点名字111","order": 111111,"value": "节点值111"}
        res=requests.put(url=u,json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    def test_dictitemdelete(self):
        '''
        字典节点删除
        :return:
        '''
        A=self.test_dictitemadd()
        u = ServerInfo.get_url('/sys/dict/item/' + A)
        res=requests.delete(url=u)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 200














