import requests

url = "https://appdev.xpandago.com/app/member/login/register/login"
payload = {'mobile':'185',
           'password':'****',
           'areaCode':'+86'}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url,params=payload,headers = headers)
print(r.url)
print(r.text)
# print(r.content)