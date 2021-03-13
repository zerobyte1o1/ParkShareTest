import requests
from cof.config import host_port
from lib.getsession import GetSession


class TenantApi():
    def __init__(self):
        self.session = GetSession().get_loginsession(1)

    def make_comment(self, content,parkingid):

        url = host_port+'admin/parkingremark/ParkingremarkController/'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With':'XMLHttpRequest'
        }
        data = {
            'content':content,
            'parkingid':parkingid

        }
        r = self.session.post(url, headers=headers, data=data)

        # print(r.json())
        return r.text



if __name__ == '__main__':
    a = TenantApi().make_comment('123',55930)
    print(a)
