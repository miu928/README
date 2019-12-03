import time
from selenium import webdriver
from AEPL.Opt.confpy import *

#设置你自己的chormedriver存放路径s
# click(element=None) 左击
# context_click(element=None) 右击
# double_click(element=None) 双击
# move_to_element(element) 移动鼠标到元素中间（悬停）
# drag_and_drop(source,target) source上按下左键拖动到target元素上
# click_and_hold(element=None) 在元素上按下鼠标左键
# release() 释放鼠标
# perform() 执行ActionChains中存储的动作

class Operater():
    def __init__(self,sectionmethod):
        self.conf = Confget(confname=os.path.abspath('./test.conf'),section= sectionmethod)
        driver_path = self.conf.GetValuestr('driver_path')#通过配置文件配置访问url
        self.driver = webdriver.Chrome(executable_path=driver_path)#实例化浏览器(启动浏览器)
        self.driver.implicitly_wait(10) #隐性的等待，对应全局

    def __getelement(self,xpath):   #获取元素 driver.find_element_by_xpath
        return self.driver.find_element_by_xpath(xpath)

    def getselector(self,classname):
        self.driver.find_element_by_css_selector(classname)

    def openURL(self):
        self.driver.get(self.conf.GetValuestr('url'))  #打开浏览器 driver.get

    def inputValue(self,value,xpath):   #获取元素对象并输入内容（value）
        self.__getelement(xpath).send_keys(value)#element.send_keys(‘需要输入的内容’) # 模拟按键输入；只针对支持输入的元素

    def click(self,xpath):
        self.__getelement(xpath).click()#获取元素对象并点击操作

    def quit(self):#关闭浏览器
        self.driver.quit()

    def maxWindow(self):#最大化浏览器
        self.maximize_window()
    

if __name__ == '__main__':
    testmission = Operater('testBaidu')
    testmission.openURL()
    testmission.inputValue('chromedriver',r'/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input')
    testmission.click(r'/html/body/div[1]/div[1]/div/div[2]/div/form/span[2]/input')
    testmission.click(r'/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a')
    time.sleep(3)#固定等待时间3s
    testmission.quit()

    test2 = Operater('51job')
    test2.openURL()
    time.sleep(3)
    test2.quit()


    
