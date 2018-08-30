import requests

reqheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
datas= {"__sid":"d476ef5538f847119cf0986439440a1a"}
# url = "http://127.0.0.1:8980/js/a/sys/user/info.json?__sid=fab8e8fd0b7d4e0b90614114182976e3"
# url = "http://127.0.0.1:8980/js/a/index.json?__sid=fab8e8fd0b7d4e0b90614114182976e3"
url = "http://127.0.0.1:8980/js/a/menuTree.json?__sid=fab8e8fd0b7d4e0b90614114182976e3"
r = requests.get(url,headers=reqheaders,data=datas)
print(r.content.decode('utf-8'))

