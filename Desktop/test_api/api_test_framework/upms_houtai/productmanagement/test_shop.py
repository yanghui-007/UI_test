import unittest
import json
import re
import requests
import os
import sys
#print(sys.path)
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#sys.path.append(os.path.dirname(__file__))
# from lib.get import get_shop
# from lib.post import post_shop
#print(sys.path)
from lib.get import get_request
from lib.post import post_request


urd='http://shop.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com'
class TestShop(unittest.TestCase):
    def test0001_6login(self):
        url=urd+'/api/auth/oauth/token?username=yanghui&password=E5PMrB0YTYRKyINrebtQdA==&grant_type=password&scope=server'
        headers={
                'Authorization':'Basic YWZyYnRjOmFmcmJ0Yw==',
                'Content-Type':'application/x-www-form-urlencoded'

        }

        res=requests.post(url=url,headers=headers)
        self.assertIn('"access_token"',res.text)
        #print(res.text)
        global token
        token=re.findall('access_token":"(.+?)",',res.text)[0]
       # print(token)

    def test0002_1Balance(self):
        url=urd+'/api/shopuser/shopUserInfo/getUserBalanceProcessDetail'
        data={
            'current':1,
            'size':20
        }
        global headers
        headers={
            "Authorization":"Bearer"+token,
           # "Content-Type":"application/x-www-form-urlencoded"
          # "Content-Type":"application/json"
          # "Content-Type":"text/plain"
        }
        
        res=requests.get(url=url,headers=headers,data=json.dumps(data))
        self.assertIn('"code":0,"msg":"success"',res.text)
        # ress=res.text
        # res_dict=json.loads(ress)
        # res_json=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#响应格式改为json格式
        # print(ress)
        # print(res_dict)
        # print(res_json)

    def test0003_getuserinfo(self):
        url=urd+'/api/shopuser/shopUserInfo/getUserInfo'
        headers={
            "Authorization":"Bearer"+token
        }

        res=requests.get(url=url,headers=headers)
        self.assertIn('"userType":0',res.text)
        self.assertIn('"username":"yanghui"',res.text)


    def test0004_getRechargeList(self):
        url=urd+"/api/shoprecharge/shopUserRecharge/getRechargeList"
        headers={
            "Authorization":"Bearer"+token
        }
        
        res=requests.get(url=url,headers=headers)
        #print(res.text)
        self.assertIn('incomeTypeName":"支付宝OTC',res.text)

    def test0005_dQueuePage(self):
        url=urd+"/api/shoporder/shopOrder/idQueuePage"
        headers={
            "Authorization":"Bearer"+token,
            "Content-Type":"application/json"
        }
        data={
            "current":1,
            "size":20,
            "query":{}
            }
        res=requests.post(url=url,headers=headers,data=json.dumps(data))
        #print(res.text)
        self.assertIn('"code":0,"msg":"success"',res.text)

    def test0006_comGiftCardTypeConf(self):
        url=urd+"/api/comsetshop/comGiftCardTypeConf/list"
        header={
            "Authorization":"Bearer"+token
        }
        data={
            "isEnableCardTypeConf":"true"
        }
        res=requests.get(url=url,headers=header,params=data)
        #print(res.text)
        self.assertIn('code":0,"msg":"success',res.text)

    #获取用户可购买商品列表
    def test0007_itemlist(self):
        url=urd+"/api/shopuser/shopUserInfo/item/list"
        headers={
            "Authorization":"Bearer"+token,
            "Content-Type": "application/json"
        }
        data='[3,4]'
        res=requests.post(url=url,headers=headers,data=data)
        #print(res.text)
        self.assertIn('code":0,"msg":"success',res.text)
    
    #卡图订单-卡密详情
    def test0008_cardDetail(self):
        url=urd+'/api/bizgift/bizGiftCardOrderCodeDetail/cardDetail'
        params={
            "cardPicDetailId":"1169452461839945730"
        }
        res=requests.get(url=url,headers=headers,params=params)
       #print(res.text)
        self.assertIn('code":0,"msg":"success',res.text)

    def test0002_2get(self,params=None,data=None):
        url=urd+'/api/shoprecharge/shopUserRecharge/getRechargeList'
        params=params
        data=data
        header=headers
        res=requests.get(url=url,headers=header,params=params,data=data)
        #print(res.text)
        self.assertIn('"code":0,"msg":"success"',res.text)

    def test0009_cardDetail(self):
        url=urd+'/api/shopuser/shopUserInfo/getUserInfo'
        #url='http://shop.c792da175267647238186842c09054706.cn-shanghai.alicontainer.com/api/shopuser/shopUserInfo/getUserInfo'
        params={
            "cardPicDetailId":"1169452461839945730"
        }

        # headers={
        #     "Authorization":"Bearer"+token
        # }
        res=get_request(self,url,headers,params=params)
        #print(res.text)
        self.assertIn('"code":0,"msg":"success"',res.text)

    def test0010_idQueuePage(self):
        url=urd+"/api/shoporder/shopOrder/idQueuePage"
        headers={
            "Authorization":"Bearer"+token,
            "Content-Type":"application/json"
        }
        data={
            "current":1,
            "size":20,
            "query":{}
            }
        params=None
        res=post_request(self,url,headers,params,json.dumps(data))
        #print(res.text)
        self.assertIn('"code":0,"msg":"success","data"',res.text)
    
if __name__=='__main__':
    unittest.main(verbosity=2)