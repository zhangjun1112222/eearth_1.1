
class ServerInfo:

    @staticmethod  #数字地球云
    def get_url(url):
        return "http://digital-earth.app.zkxqgroup.com/api/v1{}".format(url)

    @staticmethod   #v1.1的v1接口
    def get_url1(url):
        return "http://ppm-web.app.zkxqgroup.com/api/v1{}".format(url)

    @staticmethod  # v1.1的v2接口
    def get_url2(url):
        return "http://ppm-web.app.zkxqgroup.com/api/v2{}".format(url)





