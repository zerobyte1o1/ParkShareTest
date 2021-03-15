import requests
from cof.config import host_port
from lib.getsession import GetSession


class TenantApi():
    def __init__(self):
        # 注意参数
        self.session = GetSession().get_loginsession(1)

    # 查看首页
    def get_index(self):
        url = host_port + 'admin/location/map?longitude=108.953&latitude=34.277'
        res = self.session.get(url)
        return res.json()

    # 查看历史订单
    def get_order(self):
        url = host_port + 'admin/Orders/OrdersController/ByWay/?limit=5&pageNow=1'
        res = self.session.get(url)
        # print(r.json())
        return res.json()

    # 查看我的
    def get_mine(self):
        url = host_port + 'admin/tenant/findOne/'
        res = self.session.get(url)
        print(res.json())
        return res.json()

    # 下单抢车位
    def place_order(self, parkingid, sbegintime, sendTime, unitprice):
        url = host_port + 'admin/Orders/OrdersController/'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = {
            'parkingid': parkingid,
            'sbegintime': sbegintime,
            'sendTime': sendTime,
            'unitprice': unitprice
        }
        res = self.session.post(url=url, headers=headers, data=data)
        # print(res.json())
        return res.json()

    # 查看车位详情
    def get_detail(self):
        url = host_port + 'admin/parkingremark/ParkingremarkController/?parkingid=57978&pageNow=1&limit=10'
        res = self.session.get(url)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    a = TenantApi().get_order()
    print(a)
