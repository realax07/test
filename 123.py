import selenium
from selenium import webdriver as wd
import unittest as ut

class IdeTestCase(ut.TestCase):
    def setUp(self):
        self.dr = wd.Chrome("C:\My\chromedriver.exe")
        self.dr.implicitly_wait(5)
        self.dr.set_page_load_timeout(10)
        self.url = "http://ozon.ru"


    def test_main(self):
        self.dr.get(self.url)
        self.assertNotEqual(self.dr.title, "")
        print self.dr.title

    def tearDown(self):
        self.dr.quit()

if __name__ == "__main__":
    ut.main()

