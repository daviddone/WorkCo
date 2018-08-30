import requests

cookie_dict={"JSESSIONID":"CBA0AD37B43F630EB32B34B74163BCD3"}  #登录之后从cookie中提取
#将字典转为CookieJar：
cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
s = requests.Session()
s.cookies = cookies
reqheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# reqheaders = {"Host": "localhost:9990",
#     "Connection": "keep-alive",
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "http://localhost:9990",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#     "Referer": "http://localhost:9990/CBACJCPT/everisk/index.html"
#     }
# datas = {'first':'false','pn':'4','kd':'大数据'}
datas = {}
url = "http://localhost:9990/CBACJCPT/everisk/api/v4/web/strategy/game_cheater_def/apps_list"
r = s.post(url,headers=reqheaders,data=datas)
print(r.content.decode('utf-8'))