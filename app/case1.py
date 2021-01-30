# 打开雪球应用首页
# 定位首页的搜索框
# 判断搜索框是否可用，并查看搜索框name属性值
# 打印搜索框这个元素的左上角坐标和它的宽高
# 搜索框中输入：alibaba
# 判断[alibaba]是否可见
# 如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”

from appium import webdriver
import webdriver

desire_cap = {
  "platformName": "android",
  "platfromVersion":"6.0",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True    
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)

def test_attr(self):
    element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    search_enabled = element.is_enabled()
    print(element.text)
    print(element.location)
    print(element.size)
    if search_enabled == True:
        element.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        alibab_element = self.driver.find_element_by_xpath("//*[@recuse-id='com.xuqiu.android:id/name'  and *text='阿里巴巴']")
        element_display =alibaba_element.get_attribute("displayed")
        if element_display = "true":
            print("搜索成功")
        else:
            print("搜索失败")
                                                                                                     
