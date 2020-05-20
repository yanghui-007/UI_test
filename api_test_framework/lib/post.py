import unittest
import requests

def post_request(self,url,headers,params=None,data=None):
    res=requests.post(params=params,url=url,headers=headers,data=data)
    return res