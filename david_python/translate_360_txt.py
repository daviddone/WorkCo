import urllib.request
import urllib.parse
import json

def translate(content):
        url = 'http://fanyi.so.com/index/search'
        data = {
            'query': content,
            'eng': '1'
        }  # 1 英译中  0 中译英
        data = urllib.parse.urlencode(data).encode('utf - 8')
        wy = urllib.request.urlopen(url, data)
        html = wy.read().decode('utf - 8')
        ta = json.loads(html)
        print(ta['data']['fanyi'])
        return ta['data']['fanyi']
def main():
    origin_file = open("en.txt",encoding="utf-8")
    result_file = open("cn360.txt","w", encoding="utf-8")
    for item in origin_file:
        result_file.writelines(item)
        if(len(item.strip())>0):
            result_str = translate(item)
            result_file.writelines(result_str+"\n")
main()