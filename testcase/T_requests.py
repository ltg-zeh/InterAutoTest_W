import requests

r = requests.get("http://www.baidu.com")
print(r.status_code)
print(r.headers)
print(r.url)
print(r.cookies)
print(r.raw)
print(r.text)
print(r.raise_for_status())