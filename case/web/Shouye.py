# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public.login import Mylogin
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/YSscreenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'YSscreenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testShouye01(self):
        '''测试首页导航文案显示是否正常'''
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)

    def testShouye02(self):
        '''验证搜索框UI是否显示正常'''
        el1=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]')
        print(el1.get_attribute('placeholder'))
        self.assertEqual(el1.get_attribute('placeholder'),'请输入你要查找的关键字')

    def testShouye03(self):
        '''验证搜索出正确结果是否正确'''
        el1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]')
        el1.send_keys('女装')
        self.driver.find_element_by_xpath('//input[@class="but2"]').click()
        time.sleep(3)
        el2=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
        print((el2.text))
        self.assertEqual(el2.text,"毛衣女装")

    def testShouye04(self):
        '''验证搜索的内容无结果时默认文案是否显示正确'''
        el1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]')
        el1.send_keys('王麻子')
        self.driver.find_element_by_xpath('//input[@class="but2"]').click()
        time.sleep(3)
        el2=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div')
        print((el2.text))
        self.assertEqual(el2.text,"抱歉，没有找到相关的商品")

    def testShouye05(self):
        '''验证能否成功进入购物车页面'''
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/a/div/span').click()
        self.driver.implicitly_wait(10)
        el1=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/div[1]')
        el2=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[2]/div[1]')
        el3=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[3]/div[1]')
        print(el1.text)
        print(el2.text)
        print(el3.text)
        self.assertEqual(el1.text, "购物车")
        self.assertEqual(el2.text, "确认订单")
        self.assertEqual(el3.text, "完成付款")

    def testShouye06(self):
        '''验证导航中的登录是否能进入登录页面'''
        self.driver.find_element_by_xpath('//div[@class="login"]/a[1]').click()
        self.driver.implicitly_wait(5)
        el1=self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[1]/span')
        print(el1.text)
        self.assertEqual(el1.text,"用户登录")

    def testShouye07(self):
        '''验证从右侧登录入口是否进入登录页面'''
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[2]/p/a[1]').click()
        self.driver.implicitly_wait(5)
        el1=self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[1]/span')
        print(el1.text)
        self.assertEqual(el1.text,"用户登录")

    def testShouye08(self):
        '''验证导航中的注册是否能进入注册页面'''
        self.driver.find_element_by_xpath('//div[@class="login"]/a[2]').click()
        self.driver.implicitly_wait(5)
        el1 = self.driver.find_element_by_xpath('//div[@class="reg_bname"]/span')
        print(el1.text)
        self.assertEqual(el1.text, "用户注册")

    def testShouye09(self):
        '''验证从右侧注册入口是否进入注册页面'''
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[2]/p/a[2]').click()
        self.driver.implicitly_wait(5)
        el1 = self.driver.find_element_by_xpath('//div[@class="reg_bname"]/span')
        print(el1.text)
        self.assertEqual(el1.text, "用户注册")

    def testShouye10(self):
        '''验证能否从搜索框下的链接进入商品页面'''
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(5)
        el2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
        print((el2.text))
        self.assertEqual(el2.text, "毛衣女装")


    def testShouye11(self):
        '''验证商品分类能够展现下级分类'''
        el1=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/span/em')
        ActionChains(self.driver).move_to_element(el1).perform()
        el2=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/dt/div/span/a')
        ActionChains(self.driver).move_to_element(el2).perform()
        el3=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a')
        print(el3.text)
        self.assertEqual(el3.text,'儿童装')

    def testShouye12(self):
        '''验证能否从商品分类进入商品页面'''
        el1=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/span/em')
        ActionChains(self.driver).move_to_element(el1).perform()
        el2=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/dt/div/span/a')
        ActionChains(self.driver).move_to_element(el2).perform()
        el3=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a')
        ActionChains(self.driver).move_to_element(el3).perform()
        el3.click()
        el4=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]/div')
        print(el4.text)
        self.assertEqual(el4.text, '抱歉，没有找到相关的商品')

    def testShouye13(self):
        '''验证能否从精选商品的分类进入商品页面'''
        self.driver.find_element_by_xpath('//div[@class="nav_pub"]/a[2]').click()
        time.sleep(10)
        dd=self.driver.window_handles
        print(dd)
        print(self.driver.current_window_handle)
        self.driver.switch_to.window(dd[1])

        el1=self.driver.find_element_by_xpath('//div[@class="bnma"]/a[1]')
        print(el1.text)
        self.assertEqual(el1.text,"限时抢购")





if __name__ == "__main__":
    unittest.main()
