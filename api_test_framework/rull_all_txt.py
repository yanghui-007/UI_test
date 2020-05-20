import unittest
#from lib.send_email2 import send_email

#suite=unittest.defaultTestLoader.discover('testcase',pattern='test*.py')#遍历当前目录及子包中所有test*.py中所有unittest用例
#suite=unittest.defaultTestLoader.discover('testcase',pattern='test*.py')#遍历当前目录及子包中所有test*.py中所有unittest用例
suite=unittest.defaultTestLoader.discover('testcase_umps/countryproductlibrary',pattern='test*.py')#遍历当前目录及子包中所有test*.py中所有unittest用例


#生成txt文本报告：
with open("report/result.txt","w") as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite)#将输出流stream输出到文件result.txt



# unittest.TextTestRunner(verbosity=2).run(suite)
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

#send_email('report/result.txt')#发送邮件