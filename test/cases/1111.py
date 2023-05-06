import requests

from config.config import ServerInfo


def test_aircraft_commercial_pagesizi():
    """
    商用飞机管理-分页获取
    """
    res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/page/1/size/30'))
    print(res.text)