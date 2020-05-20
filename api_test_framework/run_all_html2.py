import unittest
#from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email2 import send_email
from lib.HTMLTestRunner import HTMLTestRunner
import time

now = time.strftime("%Y-%m-%d %H_%M_%S")

#遍历当前目录及子包中所有test*.py中所有unittest用例
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/countryproductlibrary',pattern='test*.py')
suite=unittest.defaultTestLoader.discover('集成后台/国家商品库',pattern='test*.py')


#1.生成html报告，方法1：
# f=open("report.html","wb")#二进制打开要生成的报告文件
# HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
# f.close()

#2.生成html报告，方法2：
with open("report/"+now+"report.html","wb") as f:#二进制打开要生成的报告文件
    HTMLTestRunner(stream=f,title="Api Test",description="测试描述：本次测试内容为小军美卡系统").run(suite)
    
send_email("report/"+now+"report.html")#发送邮件