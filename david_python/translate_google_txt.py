import requests
import execjs
import json

class Yuguii():

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def translate(content, tk):
    if len(content) > 4891:
        print("翻译文本超过限制！")
        return

    # 英==》中
    # url = "http://translate.google.cn/translate_a/single?client=t" \
    #       "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
    #       "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
    #       "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    result = requests.get(url).content.decode('utf-8')
    # print(result)
    body = json.loads(result)
    items = body[0]
    answer = ""
    for item in items:
        if(item[0] is not None):
            answer = answer + item[0]
            # print(item[0])
    print(answer)
    return answer
    # 返回的结果为Json，解析为一个嵌套列表
    # for text in body:
    #     print(text)
    # end = result.find("\",")
    # if end > 4:
    #     # print(result[4:end])
    #     return result[4:end]


def main():
    js = Yuguii()
    content = "translate"
    origin_file = open("en.txt",encoding="utf-8")
    origin_list = origin_file
    result_file = open("cn.txt","w", encoding="utf-8")
    for item in origin_file:
        result_file.writelines(item)
        if(len(item.strip())>0):
            tk = js.getTk(item)
            result_str = translate(item, tk)
            result_file.writelines(result_str+"\n")
main()


#https://blog.csdn.net/rogeshu/article/details/8944818  json parser