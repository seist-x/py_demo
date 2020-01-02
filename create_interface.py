from selenium import webdriver
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CreateInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.doclever.cn")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        driver = self.driver
        time.sleep(2)
        # driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("test_yoyo")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_id("login").click()
        time.sleep(2)
        self.assertEqual(driver.current_url,"http://www.doclever.cn/controller/console/console.html")

    def test_creat_interface(self):
        driver = self.driver
        time.sleep(5)
        #进入MyHome项目
        # driver.find_element_by_xpath("//*[contains(text(),'MyHome')]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='MyHome'])[1]/following::div[6]").click()
        #在Homework文件夹下创建接口createport
        driver.find_element_by_xpath("//div[@id='group1']/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("createport")
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='GET'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys("/user/login")
        driver.find_element_by_xpath("(//input[@type='text'])[15]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[15]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[15]").send_keys("username")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='必选'])[2]/following::span[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").send_keys("seist")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='新增'])[2]/following::button[1]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").send_keys("password")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='必选'])[3]/following::span[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").send_keys("123456")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='新增'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='运行'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='自动保存'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("www.doclever.cn")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='导入分组'])[2]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='运行'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='自动保存'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='生成'])[1]/following::span[1]").click()

    def test_logout(self):
        driver = self.driver
        time.sleep(3)
        logout = driver.find_element_by_xpath('//*[contains(text(),"test_yoyo")]')
        ActionChains(driver).move_to_element(logout).perform()  # 把鼠标放到元素上，其他的什么都不动
        time.sleep(1)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='帮助中心'])[1]/following::li[1]").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "登录"))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests[CreateInterface("test_login"),CreateInterface("test_creat_interface"),CreateInterface("test_logout")]
    runner = unittest.TextTestRunner
    runner.run(suite)