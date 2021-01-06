import requests
from utils.RequestsUtils import requests_get
from utils.RequestsUtils import requests_post
# 登录
def login():
    url = "https://appdev.xpandago.com/app/member/login/register/login"
    data = {"mobile":"18539576908","password":"123456","areaCode":"+86"}
    r = requests.get(url,params=data)
    print(r.text)
def info():
    url = "https://appdev.xpandago.com/app/member/user/user/list"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA5OTE2ODkyMzk1LCJleHAiOjE2MTA1MjE2OTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.aE9EVt619DQO-Z8PufAEHuuZRmUzHBKFfaTWWoREj_CdHY1TJQmjROvxKZNJMBULQ9d-ZhslG3L8qqtvyjmu8Q"}
    # r = requests.get(url,headers=headers)
    # print(r.text)
    r = requests_get(url,headers=headers)
    print(r)

def goodlist():
    url = "https://appdev.xpandago.com/app/goods/brand/brand/goodlist"
    data = {"brandId":"286","sidx":"person","order":"desc","page":"1"}
    r = requests.get(url,params=data)
    print(r.text)

def cart():
    url = "https://appdev.xpandago.com/app/shop/cart/buycar/saveNew"
    data = {"goodsId":"7238","num":"1","productId":"4697","goodType":"normal"}
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA5OTIzNDA5MDk2LCJleHAiOjE2MTA1MjgyMDksInVzZXJfZ3JvdXBfaWQiOm51bGx9.wQCp1A6j235VWE7tyBiZfPvCGVp_1bs8uK5Ei6OQHLRSCgtOwJcOifgY-cRTxGirXyVqKZuWPjMZVm071H7fDg"}
    # r = requests.post(url,data=data,headers=headers)
    # print(r.text)
    # print(r.json())
    r = requests_post(url,data=data,headers=headers)
    print(r)

def orderNo():
    url = "https://appdev.xpandago.com/app/order/order/order/addOrderToRedisNew"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA2MjgyMjEyMjQ3LCJleHAiOjE2MDY4ODcwMTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.6iCaPo7vqVSXUIPM0ciyYpvh25TRZSoqb0YcBtTCob3NzxZ1WuW6sN87NsV7UxrhWHVpEoJfVWb5vi7Cu1nhAA"}
    r = requests.get(url,headers=headers)
    print(r.text)

if __name__ == '__main__':
    # login()
    # info()
    # goodlist()
    cart()
    # orderNo()