# 封装的方法
# 成员方法（构造方法、析构方法）、类方法、静态方法、

class ServerInfo:

    @staticmethod  # 静态方法 类名.方法名 @:修饰符
    def get_url(url):
        return "http://cq.zkxqgroup.com:8090/api/v1{}".format(url)


# # 静态方法通过 类名.方法名
# a1 = ServerInfo.get_url("/haimo/sass/systemUser/release/getLogin")
# print(a1)


def get_url(url):
    return "http://ljtest.liuyun.tech:28080{}".format(url)

# a = get_url("/haimo/sass/systemUser/release/getLogin")
# print(a)