import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email2 import send_email
import os
import sys
sys.path.append(os.path.dirname(__file__))
#sys.path.append(os.path.join(os.path.dirname(__file__),'upms_houtai')
#from upms_houtai.country_goods.test import *
#遍历当前目录及子包中所有test*.py中所有unittest用例
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/countryproductlibrary',pattern='test*.py')
suite=unittest.defaultTestLoader.discover('upms_houtai/country_goods',pattern='test*.py')#遍历该目录下的test.py文件，并将所有test开头的用例添加到suite用例集合中


#print(suite)#打印添加到suite集合中的用例,此集合中用例，被执行一次后就消失

#1.生成html报告，方法1：
# f=open("report.html","wb")#二进制打开要生成的报告文件
# HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
# f.close()
#2.生成html报告，方法2：
with open("report/report.html","wb") as f:#二进制打开要生成的报告文件
    HTMLTestRunner(stream=f,title="Api Test",description="测试描述：本次测试内容为小军美卡系统").run(suite)

send_email('report/report.html')#发送邮件


# suite=unittest.defaultTestLoader.discover('集成后台/国家商品库',pattern='test*.py')#再次遍历该目录下的test.py文件，并将所有test开头的用例添加到suite用例集合中
# unittest.TextTestRunner(verbosity=2).run(suite)