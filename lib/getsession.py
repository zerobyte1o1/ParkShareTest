import requests
from cof.config import host_port, Account


class GetSession():

    def get_loginsession(self, flag):
        session = requests.Session()
        session.get(host_port)
        url = host_port

        if flag == 1:
            param=f'?uname={Account.gettenantname()}&pass={Account.gettenantpwd()}&imgcode={Account.CODE}'
        elif flag == 2:
            param=f'?uname={Account.getlandlordname()}&pass={Account.getlandlordpwd()}&imgcode={Account.CODE}'
        elif flag == 3:
            param=f'?uname={Account.getpropertyname()}&pass={Account.getpropertypwd()}&imgcode={Account.CODE}'
        elif flag == 4:
            param=f'?uname={Account.getplatformname()}&pass={Account.getplatformpwd()}&imgcode={Account.CODE}'
        r = session.get(url+param)
        print(r.text)
        return session


if __name__ == '__main__':
    GetSession().get_loginsession(1)
