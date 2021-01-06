
import requests
# 创建封装方法
def requests_get(url, params=None, **kwargs):
# 发送requests get请求
    r = requests.get(url,params=params,**kwargs)
# 获取相应结果
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
# 保存到字典中
    res = dict()
    res["code"] = code
    res["body"] = body
# 字典返回
    return res

# post方法封装
# 创建post方法**kwargs
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