import unittest
from commen.readfile import readfile
from cof.config import host_port
from model_api.tenantapi import TenantApi
import os

import ddt
import time


@ddt.ddt
class TenantCase(unittest.TestCase):
    # purpath = os.path.join('./data/testdata.xlsx')
    # data = readfile(purpath, 'login')
    #
    # @ddt.data(*data)
    # @ddt.unpack
    def test_lo001_api_getindex(self):
        pur = TenantApi()
        asserttext =pur.get_index()
        self.assertEqual('正常',asserttext[0]['property']['accountstatus']['accountstatusname'])




if __name__ == '__main__':

        unittest.main()
