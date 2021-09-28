import time
class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(5)

    def maoyi(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(5)
        el1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
        el1.click()
        time.sleep(3)
        dd = self.driver.window_handles
        print(dd)
        print(self.driver.current_window_handle)
        self.driver.switch_to.window(dd[1])
        time.sleep(3)

    def maoyi_xuanhao(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(5)
        el1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
        el1.click()
        time.sleep(3)
        dd = self.driver.window_handles
        print(dd)
        print(self.driver.current_window_handle)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(dd[1])
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]/em')
        el2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]/em')
        el3 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[3]/dd/a[1]/em')
        el1.click()
        el2.click()
        el3.click()
        time.sleep(5)

