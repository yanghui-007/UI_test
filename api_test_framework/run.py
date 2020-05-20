#coding=utf-8
import os
import time


k=1
while k<2:
    now_time=time.strftime('%H:%M')
    if now_time=='23:23':
        print("开始执行脚本：")
        print("执行时间为："+time.strftime('%Y_%m_%d %H:%M:%S'))
        #进入到要执行的文件的目录下，这里是绝对路径，可省略
        #os.chdir('/Users/macbook/Desktop/api_test_framework')
        #执行python命令
        os.system('python3 run_all_html.py')
        print('运行完成退出')
        break
    else:
        time.sleep(1)        
        print(time.strftime('%Y_%m_%d %H:%M:%S'))
        
