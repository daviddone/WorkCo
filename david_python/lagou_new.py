import requests
import json
import time
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

site_url ='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
reqheaders = {
              'Referer':'https://www.lagou.com/jobs/list_web?oquery=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&fromSearch=true&labelWords=relative',
              'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
}
infos = {'first':'true','pn':1,'kd':'大数据开发',"city":"北京"}  # 传递参数
r = requests.post(site_url,data=infos,headers=reqheaders)
lagou_txt = r.content.decode('utf-8')
print(lagou_txt)
lagou_json = json.loads(lagou_txt)
job_list = lagou_json['content']['positionResult']['result']
job_total_no = lagou_json['content']['positionResult']['totalCount']
pn = int(job_total_no/15)+1  # 总计页数
print(job_total_no)
print(pn)
f = open("拉勾数据分析.txt","w",encoding="utf-8")
for item in range(1,pn+1):
    infos = {'first':'true','pn':item,'kd':'大数据开发',"city":"北京"}
    all_r = requests.post(site_url, data=infos, headers=reqheaders)
    lagou_txt2 = all_r.content.decode('utf-8')
    print(lagou_txt2)
    f.writelines(lagou_txt2+"\n")
    # 每次抓取完成后,暂停一会,防止被服务器拉黑
    time.sleep(30)
f.close()