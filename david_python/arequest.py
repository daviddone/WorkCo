import requests
cookie_dict={"JSESSIONID":"87C74782D10F99DC57F91B9AEA6557FA"}  #登录之后从cookie中提取
#将字典转为CookieJar：
cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
s = requests.Session()
s.cookies = cookies
reqheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# datas = {'level':'high','page':1,'size':10}
# datas = {'level':'low','page':1,'size':10}
datas = {'level':'','page':3,'size':10}
datas = {}
datas={'__login':'true','__ajax':'json','username':'system','password':'admin'}
# url = "http://localhost:9990/CBACJCPT/everisk/api/v4/web/strategy/game_cheater_def/apps_list"
# url = "http://localhost:9990/CBACJCPT/everisk/api/v4/web/threat/dev/stat"
url = "http://localhost:9990/CBACJCPT/everisk/api/v4/web/threat/dev/list"
# url = "http://127.0.0.1:8980/js/a/login"
r = s.post(url,headers=reqheaders,data=datas)
print(r.content.decode('utf-8'))

