import requests
# 登录
def login():
    url = "https://appdev.xpandago.com/app/member/login/register/login"
    data = {"mobile":"18539576908","password":"123456","areaCode":"+86"}
    r = requests.get(url,params=data)
    print(r.text)
def info():
    url = "https://appdev.xpandago.com/app/member/user/user/list"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA2MjgyMjEyMjQ3LCJleHAiOjE2MDY4ODcwMTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.6iCaPo7vqVSXUIPM0ciyYpvh25TRZSoqb0YcBtTCob3NzxZ1WuW6sN87NsV7UxrhWHVpEoJfVWb5vi7Cu1nhAA"}
    r = requests.get(url,headers=headers)
    print(r.text)

def goodlist():
    url = "https://appdev.xpandago.com/app/goods/brand/brand/goodlist"
    data = {"brandId":"286","sidx":"person","order":"desc","page":"1"}
    r = requests.get(url,params=data)
    print(r.text)

def cart():
    url = "https://appdev.xpandago.com/app/shop/cart/buycar/saveNew"
    data = {"goodsId":"3107","num":"1","productId":"2843","goodType":"normal"}
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA2MjgyMjEyMjQ3LCJleHAiOjE2MDY4ODcwMTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.6iCaPo7vqVSXUIPM0ciyYpvh25TRZSoqb0YcBtTCob3NzxZ1WuW6sN87NsV7UxrhWHVpEoJfVWb5vi7Cu1nhAA"}
    r = requests.post(url,data=data,headers=headers)
    print(r.text)

def orderNo():
    url = "https://appdev.xpandago.com/app/order/order/order/addOrderToRedisNew"
    headers = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLmtYvor5UtVEciLCJhdWRpZW5jZSI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwidXNlcl9pZCI6MjUwNjYzLCJjcmVhdGVkIjoxNjA2MjgyMjEyMjQ3LCJleHAiOjE2MDY4ODcwMTIsInVzZXJfZ3JvdXBfaWQiOm51bGx9.6iCaPo7vqVSXUIPM0ciyYpvh25TRZSoqb0YcBtTCob3NzxZ1WuW6sN87NsV7UxrhWHVpEoJfVWb5vi7Cu1nhAA"}
    r = requests.get(url,headers=headers)
    print(r.text)

if __name__ == '__main__':
    # login()
    # info()
    # goodlist()
    # cart()
    orderNo()