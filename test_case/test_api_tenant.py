import unittest
from commen.readfile import readfile
from cof.config import host_port
from model_api.tenantapi import TenantApi
import os

import ddt
import time


@ddt.ddt
class TenantCase(unittest.TestCase):
    # 获取首页测试用例
    def test_lo001_api_getindex(self):
        pur = TenantApi()
        asserttext = pur.get_index()
        self.assertEqual('正常', asserttext[0]['property']['accountstatus']['accountstatusname'])

    # 获取历史订单测试用例
    def test_lo002_api_getorder(self):
        pur = TenantApi()
        asserttext = pur.get_order()
        self.assertEqual(0, asserttext['page']['offset'])

    # 获取我的
    def test_lo003_api_getmine(self):
        pur = TenantApi()
        asserttext = pur.get_mine()
        self.assertEqual('正常', asserttext['accountstatus']['accountstatusname'])

    # 下订单测试用例
    purpath = os.path.join('../data/testdata.xlsx')
    data = readfile(purpath, 'placeorder')

    @ddt.data(*data)
    @ddt.unpack
    def test_lo004_api_placeorder(self, parkingid, sbegintime, sendTime, unitprice):
        pur = TenantApi()
        asserttext = pur.place_order(parkingid, sbegintime, sendTime, unitprice)
        self.assertEqual('下单成功', asserttext['msg'])

    # 获取车位详细信息测试用例
    def test_lo005_api_getdetail(self):
        pur = TenantApi()
        asserttext = pur.get_detail()
        self.assertEqual(2, asserttext['total'])


if __name__ == '__main__':
    unittest.main()
