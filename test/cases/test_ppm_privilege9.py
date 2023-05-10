from config.config import ServerInfo
import requests

class TestPrivilege:
    """
    权限
    """
    def test_privilege_query(self, test_login1):
        """
        权限查询
        """
        u = ServerInfo.get_url1('/tenant/privilege/page/1/size/20')
        h = {'X-TOKEN': test_login1}
        d = {'key': '项目'}
        res = requests.get(url=u, headers=h, json=d)
        assert res.status_code == 200
        assert res.json()['code'] == 200