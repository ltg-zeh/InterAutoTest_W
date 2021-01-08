import requests
from utils.RequestsUtils import requests_get
from utils.RequestsUtils import requests_post
from utils.RequestsUtils import Request
# 登录
def login():
    url = "https://appdev.xpandago.com/app/member/login/register/login"
    data = {"mobile":"18539576908","password":"123456","areaCode":"+86"}

    request = Request()
    r = request.get(url,params=data)
    print(r)

# 个人信息
def info():
    url = "https://appdev.xpandago.com/app/member/user/user/list"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA5OTE2ODkyMzk1LCJleHAiOjE2MTA1MjE2OTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.aE9EVt619DQO-Z8PufAEHuuZRmUzHBKFfaTWWoREj_CdHY1TJQmjROvxKZNJMBULQ9d-ZhslG3L8qqtvyjmu8Q"}

    request = Request()
    r = request.get(url,headers=headers)
    print(r)

# 商品列表
def goodlist():
    url = "https://appdev.xpandago.com/app/goods/brand/brand/goodlist"
    data = {"brandId":"286","sidx":"person","order":"desc","page":"1"}

    request = Request()
    r = request.get(url,params=data)
    print(r)

# 购物车
def cart():
    url = "https://appdev.xpandago.com/app/shop/cart/buycar/saveNew"
    data = {"goodsId":"7238","num":"1","productId":"4697","goodType":"normal"}
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA5OTIzNDA5MDk2LCJleHAiOjE2MTA1MjgyMDksInVzZXJfZ3JvdXBfaWQiOm51bGx9.wQCp1A6j235VWE7tyBiZfPvCGVp_1bs8uK5Ei6OQHLRSCgtOwJcOifgY-cRTxGirXyVqKZuWPjMZVm071H7fDg"}

    request = Request()
    r = request.post(url,data=data,headers=headers)
    print(r)

# 订单
def orderNo():
    url = "https://appdev.xpandago.com/app/order/order/order/addOrderToRedisNew"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA5OTE2ODkyMzk1LCJleHAiOjE2MTA1MjE2OTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.aE9EVt619DQO-Z8PufAEHuuZRmUzHBKFfaTWWoREj_CdHY1TJQmjROvxKZNJMBULQ9d-ZhslG3L8qqtvyjmu8Q"}

    request = Request()
    r = request.get(url,headers=headers)
    print(r)

if __name__ == '__main__':
    login()
    info()
    goodlist()
    cart()
    orderNo()