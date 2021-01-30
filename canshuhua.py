from appium import webdriver
import pytest

class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = ['Android']
        desired_caps['platfromVersion'] = ['6.0']
        desired_caps['deviceName'] = ['127.0.0.1:7555']
        desired_caps['appPackage'] = ['com.xueqiu.android']
        desired_caps['appActivity'] = ['com.xueqiu.android.common.MainActivity']
        desired_caps['noReset'] = True    #不处理缓存
        desired_caps['skipServerInstallation'] = True  #跳过一些安装
        desired_caps['unicodeKeyBord'] = 'true' #输入中文
        desired_caps['reseKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(10)
def teardown(self):
    pass
def test_search(self):
    """
    1、打开雪球app
    2、点击搜索框
    3、输入搜索词'alibaba'/'xiaomi'
    4、点击第一个搜索结果
    5、判断股票价格
    """
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click
    current_price = self.driver.find_element(MobileBy.XPATH,"//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    expect_price = 240  #期望股价
    assert_that(current_price.close_to(expect_price.expect_price*0.5))  #股价浮动

@pytest.mark.paramentrize('searchkey, type, expect_price',[
    ('alibaba', 'BABA', '240'),
    ('xiaomi', '08180', '31')
])
def test_search(self，searchkey, type, expect_price):
    """
    1、打开雪球app
    2、点击搜索框
    3、输入搜索词'alibaba'/'xiaomi'
    4、点击第一个搜索结果
    5、判断股票价格
    """
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("searchkey")
    self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click
    current_price = self.driver.find_element(MobileBy.XPATH,"//*[@text='type']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    
    assert_that(current_price.close_to(expect_price.expect_price*0.5))  #股价浮动
    
def hahh:
    