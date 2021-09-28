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

    # def testShangpingxz_01(self):
    #     '''验证选择商品品牌是否匹配显示出来的商品'''
    #     Mylogin(self.driver).login()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/dl/dd/a[3]').click()
    #     time.sleep(3)
    #     el1=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
    #     print(el1.text)
    #     self.assertEqual(el1.text,'格子裙')
    #
    # def testShangpingxz_02(self):
    #     '''验证排序的方式是否有效排序'''
    #     Mylogin(self.driver).login()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[1]/a[2]').click()
    #     time.sleep(3)
    #     el1=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
    #     print(el1.text)
    #     self.assertEqual(el1.text,"毛衣女装")
    #
    # def testShangpingxz_03(self):
    #     '''验证能否进入特定商品购买页面-毛衣女装'''
    #     Mylogin(self.driver).login()
    #     time.sleep(3)
    #     el1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
    #     el1.click()
    #     time.sleep(3)
    #     dd=self.driver.window_handles
    #     print(dd)
    #     print(self.driver.current_window_handle)
    #     self.driver.switch_to.window(dd[1])
    #     time.sleep(3)
    #     el2=self.driver.find_element_by_xpath('//div[@class="info"]/h1')
    #     print(el2.text)
    #     self.assertEqual(el2.text, "毛衣女装")
    #
    # def testShangpingxz_04(self):
    #     '''验证是否能选择商品款式'''
    #     Mylogin(self.driver).maoyi()
    #     time.sleep(2)
    #     el1=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]/em')
    #     el2=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]/em')
    #     el3=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[3]/dd/a[1]/em')
    #     el1.click()
    #     el11=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]')
    #     el2.click()
    #     el22=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]')
    #     el3.click()
    #     el33=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[3]/dd/a[1]')
    #     time.sleep(5)
    #     self.assertEqual(el11.get_attribute('class'), 'selected')
    #     self.assertEqual(el22.get_attribute('class'), 'selected')
    #     self.assertEqual(el33.get_attribute('class'), 'selected')
    #
    # def testShangpingxz_05(self):
    #     '''验证是否能正常输入数量'''
    #     Mylogin(self.driver).maoyi()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//*[@id="buy_num"]').clear()
    #     self.driver.find_element_by_xpath('//*[@id="buy_num"]').send_keys('4')
    #     el1=self.driver.find_element_by_xpath('//*[@id="buy_num"]')
    #     print(el1.get_attribute('value'))
    #     self.assertEqual(el1.get_attribute('value'),'4')
    #
    # def testShangpingxz_06(self):
    #     '''验证是否能正常选中数量'''
    #     Mylogin(self.driver).maoyi()
    #     time.sleep(2)
    #     # self.driver.find_element_by_xpath('//*[@id="buy_num"]').clear()
    #     el1=self.driver.find_element_by_id('num_plus')
    #     el1.click()
    #     el1.click()
    #     el1.click()
    #     time.sleep(5)
    #     el2 = self.driver.find_element_by_xpath('//*[@id="buy_num"]')
    #     print(el2.get_attribute('value'))
    #     self.assertEqual(el2.get_attribute('value'), '4')
    #
    # def testShangpingxz_07(self):
    #     '''验证能否正常加入购物车'''
    #     Mylogin(self.driver).maoyi_xuanhao()
    #     self.driver.find_element_by_xpath('//a[@class="yyue nowbuy"]').click()
    #     time.sleep(3)
    #     el1=self.driver.find_element_by_xpath('//div[@class="buy_tip_name"]/p')
    #     print(el1.text)
    #     self.assertEqual(el1.text,'宝贝已成功添加到购物车')

    def testShangpingxz_08(self):
        '''验证能否直接购买-提示登录'''
        Mylogin(self.driver).maoyi_xuanhao()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/a[2]').click()
        time.sleep(10)
        el1=self.driver.find_element_by_xpath('//div[@id="login_user"]/span')
        print(el1.text)
        time.sleep(3)
        self.assertEqual(el1.text,'用户登陆')
    #
    # def testShangpingxz_09(self):
    #     '''验证能否正常查看商品评价'''
    #     Mylogin(self.driver).maoyi()
    #     self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[2]/div/div[1]/a[2]').click()
    #     time.sleep(3)
    #     el1=self.driver.find_element_by_xpath('//div[@class="comMenu"]/a[1]')
    #     print(el1.text)
    #     self.assertEqual(el1.text,'全部评价（0）')


if __name__ == "__main__":
        unittest.main()