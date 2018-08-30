import requests

reqheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
datas= {"key":"4f3e4eee3efe05aa8593e438df8aed22","ip":"106.38.121.194","output":"JSON"}
# url = "http://127.0.0.1:8980/js/a/sys/user/info.json?__sid=fab8e8fd0b7d4e0b90614114182976e3"
# url = "http://127.0.0.1:8980/js/a/index.json?__sid=fab8e8fd0b7d4e0b90614114182976e3"
url = "https://restapi.amap.com/v3/ip?ip=114.247.50.2&output=JSON&key=4f3e4eee3efe05aa8593e438df8aed22"
r = requests.get(url,headers=reqheaders)
print(r.content.decode('utf-8'))

