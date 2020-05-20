import unittest
import requests
import re
import json

def get_request(self,url,headers=None,params=None,data=None):
    # url=url
    # headers=headers
    # params=params
    # data=data
    res=requests.get(url=url,headers=headers,params=params,data=data)
    return res


    #return(requests.get(url=url,headers=headers,params=params,data=data))
    #print(res.text)
    