#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from business.tpa_business import Tpa_Business
#from business.Tkinter_business
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
import traceback
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import pyautogui #鼠标点击
import datetime
import os
import HTMLTestRunner_cn
import unittest
#from util.emailtest import Run_Send_Mail
from util.MyLogger import My_Log
from util.information_data import New_Data
class Tpa_Simple_Case(unittest.TestCase):
    '''Tpa 测试报告'''
    @classmethod
    def setUpClass(cls): 
        cls.chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
        os.popen(cls.chrome_exe)
        cls.chrome_options = Options()
        cls.chrome_options.add_argument('--start-maximized')
        cls.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        cls.driver = webdriver.Chrome(cls.chrome_driver, chrome_options=cls.chrome_options)
        cls.driver.get('https://tpatest.ikandy.cn/')
    @classmethod
    def tearDownClass(cls):
        pass

    def add_img(self):
        self.imgs.append(cls.driver.get_screenshot_as_base64())
        return True
    def setUp(self):
        self.imgs=[]
        self.messges = New_Data()
        self.Tpa = Tpa_Business(self.driver)
    def tearDown(self):
        time.sleep(2)
        print('结束')
    def test_1loging_success(self):
        '''Tpa 登录验证'''
        success = self.Tpa.tpa_login_base('testyzc','123456')
        self.add_img()
        self.assertFalse(success)
    unittest.skip('现在不需要')
    def test_2creat_case(self):
        '''创建一个新的案件'''
        for i in range(4,6):
            self.Tpa.tpa_creat_case_base('310107199306238673','2020-07-28 10:00:00',i,2)#,'18312341234',self.messges.get_address(),self.messges.get_text())
            time.sleep(1)
        self.Tpa.tpa_creat_case_base('140101196404043286','2020-07-29 10:00:00',5,2)
        self.add_img()
    @unittest.skip('现在不需要')
    def test_3search_case(self):
        '''验证搜索案件功能'''
        self.Tpa.tap_worktop_base('')
    #@unittest.skip('现在不需要')
    def test_5Insurance_case(self):
        '''定损处理任务'''
        #self.Tpa.tap_worktop_job_receive()
        self.Tpa.tap_wirktop_job_check()
    @unittest.skip('现在不需要')
    def test_4case_detail_data(self):
        '''案件详情'''
        result_text = self.Tpa.tpa_case_detail_base('1234','测试内容123456测试','测试内容64321测试')
        self.add_img()
        self.assertIn('',result_text,msg='断言')
        self.add_img()
    def test_6case(self):
        '''定损任务处理'''
        self.Tpa.tap_case_dingsun_base()
    @unittest.skip('现在不需要退出')
    def test_9exit_quit_case(self):
        '''验证是否可以正常退出'''
        self.Tpa.tap_exit_base()



if __name__ == '__main__':
    unittest.main()



