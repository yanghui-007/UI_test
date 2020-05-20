
#1.访问百度，进行搜索
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
#driver.quit()
'''



#2.控制浏览器窗口大小
'''
#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://m.mail.10086.cn")
#参数数字为像素点
print ("设置浏览器宽 480、高 800 显示")
#driver.set_window_size(480, 800)
driver.maximize_window()
#driver.quit()
'''



#3.控制浏览器后退、前进
'''
from selenium import webdriver
driver = webdriver.Chrome()
#访问百度首页
first_url= 'http://www.baidu.com'
print ("now access %s"%first_url)
driver.get(first_url)
#访问新闻页面
second_url='http://news.baidu.com'
print ("now access %s" %second_url)
driver.get(second_url)
#返回（后退）到百度首页
print("back to %s "%first_url) 
driver.back()
#前进到新闻页
print ("forward to %s"%second_url)
driver.forward()
#driver.quit()
'''



#4.简单元素操作
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://upms.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/#/login")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[1]/div/div/input").clear()
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[1]/div/div/input").send_keys("yanghui")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div/div/input").clear()
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div/div/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[4]/div/button").click()
#driver.quit()
'''
#5.WebElement 接口常用方法
'''
#常用方法1:submit()
#注：submit()方法用于提交表单，这里特别用于没提交按钮的情况，例如搜索框输入关键字之后的“回车”操作，那么就可以通过 submit()来提交搜索框的内容。
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
driver.find_element_by_id('translateContent').send_keys('hello')
#提交输入框的内容
driver.find_element_by_id('translateContent').submit()
#driver.quit()
'''

'''
#常用方法2:
#size 返回元素的尺寸。
#text 获取元素的文本。
#get_attribute(name) 获得属性值。
#is_displayed() 设置该元素是否用户可见。
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#获得输入框的尺寸
size=driver.find_element_by_id('kw').size
print(size)
#返回百度页面底部备案信息
text=driver.find_element_by_id("s-bottom-layer-right").text
print(text)
#返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
attribute=driver.find_element_by_id("kw").get_attribute('name')
print(attribute)
#返回元素的结果是否可见，返回结果为 True 或 False
result=driver.find_element_by_id("kw").is_displayed()
print(result)
#driver.quit()
'''

#6.鼠标事件
#ActionChains 类提供的鼠标操作的常用方法：
#perform() 执行所有 ActionChains 中存储的行为
#context_click() 右击
#double_click() 双击
#drag_and_drop() 拖动
#move_to_element() 鼠标悬停

'''
#常用方法1:鼠标右击操作
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#定位到要右击的元素
right_click =driver.find_element_by_xpath("//*[@id='s-top-left']/a[1]")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
#driver.quit()
'''

'''
#常用方法2:鼠标悬停
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#定位到要悬停的元素
above =driver.find_element_by_xpath("//*[@id='s-top-left']/div/a")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()
driver.quit()
'''

'''
#常用方法3:鼠标双击操作
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#定位到要悬停的元素
double_click = driver.find_element_by_xpath('//*[@id="hotsearch-refresh-btn"]/i')
#对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()
driver).move_to_element(above).perform()
driver.quit()
'''

'''
#常用方法4:鼠标推放操作
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#定位元素的源位置
element = driver.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div')
#定位元素要移动到的目标位置
target = driver.find_element_by_id("kw")
#执行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()
'''

'''
#常用方法5:键盘事件
from selenium import webdriver
import time
#引入 Keys 模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(3)
#删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#输入空格键+“教程”
time.sleep(1)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(1)
driver.find_element_by_id("kw").send_keys("教程")
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
#ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)
#通过回车键盘来代替点击操作
#driver.find_element_by_id("su").send_keys(Keys.ENTER)
#driver.quit()
'''


'''
#7.获得验证信息:我们用得最多的几种验证信息分别是 title 、URL 和 text，
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://upms.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/#/login")
print('Before login================')
#打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#执行邮箱登录
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("yanghui")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
print('After login================')
#再次打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#获得登录的用户名
time.sleep(3)
user = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[3]').text
print(user)
time.sleep(3)
driver.quit()
'''


#8.设置元素显示等待
'''
#例1:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = WebDriverWait(driver,5,0.5).until(
EC.presence_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
driver.quit()
'''

'''
#例2:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://upms.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/#/login")
print('Before login================')
#打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#执行邮箱登录
#driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').clear()
#driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("yanghui")
element1 = WebDriverWait(driver,9,0.5).until(
EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div/div/div[2]/div/form/div[1]/div/div/input"))
)
element1.clear()
element1.send_keys("yanghui")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
print('After login================')
#再次打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#获得登录的用户名
#user = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[3]').text
element2 = WebDriverWait(driver,5,0.5).until(
EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div/div[1]/div/div[3]/div[3]"))
)
element2.text
print(user)
driver.quit()
'''

#9.隐式等待
'''
#例1:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw")
input_.send_keys('selenium')
driver.quit()
'''

'''
#例2:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://upms.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/#/login")
print('Before login================')
#打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#执行邮箱登录
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("yanghui")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
print('After login================')
#再次打印当前页面 title
title = driver.title
print(title)
#打印当前页面 URL
now_url = driver.current_url
print(now_url)
#获得登录的用户名
user = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[3]').text
print(user)
driver.quit()
'''

#10.sleep 休眠方法
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(2)
driver.find_element_by_id("kw").send_keys("webdriver")
#print(driver.find_element_by_id("kw"))
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()
'''


#11.定位一组元素
'''
from selenium import webdriver
import os
import sys
driver = webdriver.Chrome()
#print(os.path.abspath(__file__))

#print(os.path.abspath(".."))
print(os.path.abspath("."))
file_path = 'file:///' + os.path.abspath('checkbox.html')
print(file_path)
#sys.path.append(os.path.join(os.path.dirname(__file__),'checkbox.html'))
#file_path='file:///' + '/Users/macbook/Desktop/api_test_framework/集成后台/国家商品库/checkbox.html'
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
#driver.quit()
'''

'''
from selenium import webdriver
import os
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
#通过 XPath 找到 type=checkbox 的元素
#checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
#通过 CSS 找到 type=checkbox 的元素
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
print(checkboxes)
for checkbox in checkboxes:
        checkbox.click()
# 打印当前页面上 type 为 checkbox 的个数
print (len(checkboxes))
# 把页面上最后 1 个 checkbox 的勾给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
driver.quit()
'''

#12.多表单切换
'''
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)
#切换到 iframe（id = "if"）
driver.switch_to_frame("if")
#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
#driver.quit()
'''


#13.多窗口切换
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
driver.maximize_window()
#获得百度搜索窗口句柄
sreach_windows= driver.current_window_handle
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u"立即注册").click()
#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
#进入注册窗口
for handle in all_handles:
        if handle != sreach_windows:
                driver.switch_to_window(handle)
                print ('now register window!')
                driver.find_element_by_name("userName").send_keys('username')
                driver.find_element_by_name('password').send_keys('password')
#……
#进入搜索窗口
for handle in all_handles:
        if handle == sreach_windows:
                driver.switch_to_window(handle)
                print ('now sreach window!')
                driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
                driver.find_element_by_id("kw").send_keys("selenium")
                driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
'''

#14.警告框处理
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
#鼠标悬停相“设置”链接
link = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(link).perform()
#打开搜索设置
driver.find_element_by_class_name('setpref').click()
#保存设置
driver.find_element_by_css_selector('#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary').click()
#接收弹窗
driver.switch_to_alert().accept()
driver.quit()
'''


#15.上传文件
'''
#普通上传：普通的附件上传都是将本地文件的路径作为一个值放 input 标签中，通过 form 表单提交的
# 时候将这个值提交给服务器。
# 插件上传：一般是指基于 Flash 与 JavaScript 或 Ajax 等技术所实现的上传功能或插件。

#普通上传：send_keys 实现上传
from selenium import webdriver
import os
driver = webdriver.Chrome()
#打开上传功能页面
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('/Users/macbook/Desktop/反欺诈.xmind')
#driver.quit()
'''

#16.下载文件
#可通过设置功能，设置文件默认下载路径

#17.操作 Cookie
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
#driver.get("http://www.youdao.com")
driver.get("http://www.baidu.com")
# 获得 cookie 信息
cookie= driver.get_cookies()
#将获得 cookie 的信息打印
print(cookie)
driver.quit()
'''
#18.调用 JavaScript
'''
from selenium import webdriver
import time
#访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js_="var q=document.documentElement.scrollTop=0"
driver.execute_script(js_)
time.sleep(3)
#driver.quit()
'''
#19窗口截图
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
try:
    driver.find_element_by_id('kw_error').send_key('selenium')
    driver.find_element_by_id('su').click()
except :
    driver.get_screenshot_as_file("/Users/macbook/Desktop/baidu_error2.jpg")
    driver.quit()
'''
#20.关闭窗口
'''
在前页的例子中我们一直在使用 quit()方法，其含义为退出相关的驱动程序和关闭所有窗口。除此之
外 WebDriver 还提供了 close()方法，用于关闭当前窗口。当脚本在执行时打开了多个窗口，如本章的第 10
小节多窗口的处理，这个时候只能关闭其中的某一个窗口，这个时候就需要使用 close()来关闭。
'''
#21.验证码的处理
'''
对验证码的常见处理方式有以下几种。
去掉验证码
这是最简单的方法，对于开发人员来说，只是把验证码的相关代码注释掉即可，如果是在测试环境，
这样做可省去了测试人员不少麻烦，如果自动化脚本是要在正式环境跑，这样就给系统带来了一定的风险。
设置万能码
去掉验证码的主要是安全问题，为了应对在线系统的安全性威胁，可以在修改程序时不取消验证码，
而是程序中留一个“后门”---设置一个“万能验证码”，只要用户输入这个“万能验证码”，程序就认为
验证通过，否则按照原先的验证方式进行验证。
'''

#21.WebDriver 原理
#在 Python 提供了 logging 模块，logging 模块给运行中的应用提供了一个标准的信息输出接口。它提供
# 了 basicConfig()方法用于基本信息的定义。将 debug 模块开启。就可以捕捉到客户端与服务器的交互信息。
# 运行脚本，basicConfig()所捕捉的 log 信息。不过 basicConfig()开启的 debug 模式只能捕捉到客户端向
# 服务器所发送的 POST 请求，而无法获取服务器所返回应答信息。
from selenium import webdriver
import logging
logging.basicConfig(level=logging.DEBUG)
diver = webdriver.Chrome()
diver.get("http://www.baidu.com")
diver.find_element_by_id("kw").send_keys("selenium")
diver.find_element_by_id("su").click()
diver.quit()