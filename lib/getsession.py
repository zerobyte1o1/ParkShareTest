import requests
from cof.config import host_port, Account


class GetSession():
    # 获取各个账户登陆后的session
    def get_loginsession(self, flag):
        session = requests.Session()
        session.get(host_port+'image')
        url = host_port
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.82Safari / 537.36',
            'X-Requested-With': 'XMLHttpRequest',


        }

        if flag == 1:
            param = f'login?uname={Account.gettenantname()}&upass={Account.gettenantpwd()}&imgcode={Account.CODE}'
        elif flag == 2:
            param = f'login?uname={Account.getlandlordname()}&upass={Account.getlandlordpwd()}&imgcode={Account.CODE}'
        elif flag == 3:
            param = f'login?uname={Account.getpropertyname()}&upass={Account.getpropertypwd()}&imgcode={Account.CODE}'
        elif flag == 4:
            param = f'login?uname={Account.getplatformname()}&upass={Account.getplatformpwd()}&imgcode={Account.CODE}'
        r = session.get(url=url + param, headers=headers)
        print(r.json())
        return session


if __name__ == '__main__':
    GetSession().get_loginsession(1)
