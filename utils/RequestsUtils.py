
import requests
from utils.logUtils import my_log
# get方法封装
def requests_get(url, params=None, **kwargs):
# 发送requests get请求
    r = requests.get(url,params=params,**kwargs)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
# 保存到字典中
    res = dict()
    res["code"] = code
    res["body"] = body

    return res

# post方法封装
def requests_post(url, data=None, json=None, **kwargs):
    r = requests.post(url, data=data, json=json, **kwargs)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # body = r.text
    res = dict()
    res["code"] = code
    res["body"] = body
    return res

class Request:
    # 定义公共方法
    def __init__(self):
        self.log = my_log("Requests")
    def requests_api(self,url, params=None, data=None, json=None,method='get',**kwargs,):
        if method == "get":
            # get请求
            self.log.debug("发送get请求")
            r = requests.get(url, params=params, **kwargs)
        elif method == "post":
            # post请求
            self.log.debug("发送post请求")
            r = requests.post(url, data=data, json=json, **kwargs)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res
    # get方法
    def get(self,url,**kwargs):
        return self.requests_api(url,method="get",**kwargs)
    # post方法
    def post(self,url,**kwargs):
        return self.requests_api(url,method="post",**kwargs)