# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver as wd
import unittest
from selenium.webdriver.common.proxy import *


class Ide(unittest.TestCase):
    def setUp(self):
        # myProxy = "proxy.ozon.ru:3128"
        # proxy = Proxy({
        #     'proxyType': ProxyType.MANUAL,
        #     'httpProxy': myProxy,
        #     'ftpProxy': myProxy,
        #     'sslProxy': myProxy,
        #     'noProxy': ''
        # })
        self.d = wd.Firefox()
        # self.d.implicitly_wait(5)
        self.url = "http://ozon.qa.ozon"

    def test_1(self):
        self.d.get(self.url)
        self.assertNotEqual(self.d.title, "")
        print self.d.title

    def tearDown(self):
        self.d.close()

if __name__ == "__main__":
    unittest.main()
