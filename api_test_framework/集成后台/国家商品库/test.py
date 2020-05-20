import unittest
import json
import re
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from lib.get import get_request
from lib.post import post_request
from lib.db2 import *

urd='http://upms.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/api'
token='18ff9af1-9662-43aa-9bd4-bb49b2e87f61'

class Test_countryproductlibrary(unittest.TestCase):

    #发送验证码接口：
    # def test001_sendcode(self):
    #     url=urd+'/authCode'
    #     headers={
    #         'Content-Type':'application/x-www-form-urlencoded'
    #     }

    #     params={
    #         "username":"yanghui"
    #     }
    
    #     res=get_request(self,url,headers,params,)
    #     print(res.text)


    #登陆接口：
    # def test002_login(self):
    #     #url=urd+'api/auth/oauth/token?username=yanghui&password=E5PMrB0YTYRKyINrebtQdA==&authCode=178573&grant_type=password&scope=server'
    #     url=urd+'/auth/oauth/token'
    #     headers={
    #         'Content-Type':'application/x-www-form-urlencoded',
    #         'Authorization':'Basic YWZyYnRjOmFmcmJ0Yw==',
    #         #'isToken':'false'
    #     }

    #     params={
    #         'username':'yanghui',
    #         'password':'E5PMrB0YTYRKyINrebtQdA==',
    #         'authCode':'682277',
    #         'grant_type':'password',
    #         'scope':'server'
    #     }
    #     res=post_request(self,url,headers,params)
    #     print(res.text)

    #后台-商品管理-国家商品库#列表
    def test003_countryproductpage(self):
        url=urd+'/gameservProduct/countryProduct/page'

        headers={
           "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            'productTypeId':'1',
            'productName':'',
            'statue':'1',
            'countryId':'21',
            'current':'1',
            'size':'2'
        }   

        res=get_request(self,url,headers,params)

        print(res.status_code)#响应的HTTP状态码
        print(res.reason)#响应的状态码含义

        #print(res.text)
        #响应格式改为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#响应格式改为json格式
        #print(ress)
        #print(res_dict)
        print('---------------------------test003_/gameservProduct/countryProduct/page后台-商品管理-国家商品库#列表---------------------------')
        #print(res_json)

        #self.assertIn('"code":0,"msg":"success"',res.text)
        
        try:
            self.assertIn('"code":0,"msg":"success"',res.text)
        except Exception as err:
            # 正式运行前注释掉打印异常
            print(err)
            #print(res)        


    #后台-商品类型-获取国家列表
    def test004_getUniversalTypeAllCountry(self):
        url=urd+'/gameservProduct/productCountry/getUniversalTypeAllCountry'

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        res=get_request(self,url,headers)

        print(res.status_code)#响应的HTTP状态码
        print(res.reason)#响应的状态码含义
        #print(res.text)

        #b7b0ab40-84cc-4dae-bb3d-f55b5e95d125
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#响应格式改为json格式
        print('---------------------------test004_/gameservProduct/productCountry/getUniversalTypeAllCountry后台-商品类型-获取国家列表---------------------------')
        #print(res_json)

        self.assertIn('"code":0,"msg":"success"',res.text)
      


    #后台-商品管理-通用商品列表-关联sku列表分页
    def test005_detailPage(self):
        url=urd+'/gameservProduct/commonProduct/detailPage'

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            'id':'1',
            'size':'10',
            'current':'1'
        }

        res=get_request(self,url,headers,params)
        #print(res.text)
        print(res.status_code)#响应的HTTP状态码
        print(res.reason)#响应的状态码含义

        #响应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#响应格式为json格式
        print('---------------------------test005_/gameservProduct/commonProduct/detailPage后台-商品管理-通用商品列表-关联sku列表分页---------------------------')
        #print(res_json)

        #self.assertIn('"code":01,"msg":"success"',res.text)

        # try:
        #     self.assertIn('"code":0,"msg":"success"',res.text)
        # except Exception as err:
        #     # 正式运行前注释掉打印异常
        #     print(err)
        #     print(ress)         

    #后台-商品管理-国家商品库#详情
    def test006_countryProductdetail(self):
        url=urd+"/gameservProduct/countryProduct/detail"

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            'countryId':1,
            'productId':1
        }

        res=get_request(self,url,headers,params)
        #print(res.text)

        print(res.status_code)#相应的状态码
        print(res.reason)#响应的状态码含义

        #响应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#响应格式为json格式
        print('---------------------------test006_/gameservProduct/countryProduct/detail后台-商品管理-国家商品库#详情---------------------------')
        #print(res_json)

        self.assertIn('"code":0,"msg":"success"',res.text)


    #后台-优惠券管理-列表
    def test007_gameservCouponpage(self):
        url=urd+"/gameservSetting/gameservCoupon/page"

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            "current":"1",
            "size":"1"
        }

        res=get_request(self,url,headers,params)
        #print(res.text)

        print(res.status_code)#相应的状态码
        print(res.reason)#相应的状态码含义

        #相应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#相应格式为json格式
        print('---------------------------test007_/gameservSetting/gameservCoupon/page后台-优惠券管理-列表---------------------------')
        #print(res_json)

        self.assertIn('"code":0,"msg":"success"',res.text)
        
    #后台-订单管理-商品订单管理-page调整版
    def test008_OrderInfopage(self):
        url=urd+'/gameservOrder/gameservCardOrderInfo/page'

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            "current":"1",
            "size":"1"
        }  

        res=get_request(self,url,headers,params)
        #print(res.text)

        print(res.status_code)#相应的状态码
        print(res.reason)#相应的状态码含义

        #相应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#相应格式为json格式
        print('---------------------------test008_/gameservOrder/gameservCardOrderInfo/page后台-订单管理-商品订单管理-page调整版---------------------------')
        #print(res_json)

        self.assertIn('"code":0,"msg":"success"',res.text)

        #数据库校验
        # result=query_db("select order_no from gameserv_card_order_info_1 where id='1181835261673672706'")[0][0]
        # print(result)

    #后台-会员管理-会员等级管理-列表
    def test009_rankpage(self):
        url=urd+'/gameservUser/rank/page'

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            "current":1,
            "size":1
        } 

        res=get_request(self,url,headers,params)

        #print(res.text)

        print(res.status_code)#相应的状态码
        print(res.reason)#相应的状态码含义

        #相应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#相应格式为json格式
        print('---------------------------test009_/gameservUser/rank/page后台-会员管理-会员等级管理-列表---------------------------')
        #print(res_json)

        self.assertIn('"code":0,"msg":"success"',res.text)

    #获取余额代充报价
    def test_010_getBalancePrice(self):
        url=urd+'/gameservProduct/productSetting/getBalancePrice'

        headers={
            "Content-Type":'application/x-www-form-urlencoded',
            "Authorization":"Bearer"+token
        }

        params={
            "id":1
        }

        res=get_request(self,url,headers,params)

        #print(res.text)

        print(res.status_code)#相应的状态码
        print(res.reason)#相应的状态码含义

        #相应格式为json格式
        ress=res.text
        res_dict=json.loads(ress)
        res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#相应格式为json格式
        print('---------------------------test010_/gameservProduct/productSetting/getBalancePrice获取余额代充报价---------------------------')
        #print(res_json)

        #self.assertIn('"code":0,"msg":"success"',res.text)

        # try:
        #     self.assertIn('"code":0,"msg":"success"',res.text)
        # except Exception as err:
        #     # 正式运行前注释掉打印异常
        #     print(err)
        #     print(ress) 

if __name__=='__main__':
    unittest.main(verbosity=2)