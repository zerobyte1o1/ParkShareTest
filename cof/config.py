# 云服务器地址
host_port = "http://121.4.57.246:8080/SharedParkingPlace/"
# 测试范围 ui api 空为全部
scope = 'api'




# 登陆数据
class Account:
    # 抢租客测试账号
    TENANT = {'name': '抢租客0', 'pwd': '123'}
    # 出租方测试账号
    LANDLORD = {'name': '出租方1', 'pwd': '123'}
    # 物业方测试账号
    PROPERTY = {'name': '物业0', 'pwd': '123'}
    # 平台方测试账号
    PLATFORM = {'name': 'pt', 'pwd': '123'}
    # 验证码
    CODE = '0000'

    @classmethod
    def gettenantname(cls):
        return cls.TENANT['name']

    @classmethod
    def gettenantpwd(cls):
        return cls.TENANT['pwd']

    @classmethod
    def getlandlordname(cls):
        return  cls.LANDLORD['name']

    @classmethod
    def getlandlordpwd(cls):
        return cls.LANDLORD['pwd']

    @classmethod
    def getpropertyname(cls):
        return cls.PROPERTY['name']

    @classmethod
    def getpropertypwd(cls):
        return cls.PROPERTY['pwd']

    @classmethod
    def getplatformname(cls):
        return cls.PLATFORM['name']

    @classmethod
    def getplatformpwd(cls):
        return cls.PLATFORM['pwd']

    @classmethod
    def getcode(cls):
        return cls.CODE


if __name__ == '__main__':
    print(Account.gettenantname())
