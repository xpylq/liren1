import urllib
import json


def get_proxy():
    try:
        content = urllib.request.urlopen(
            "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=0d227b71f4a24da49dd3f0faf9e3b9e0&orderno=MF20186110532QdJOcV&returnType=2&count=1").read()
        proxy_list = json.loads(content)["RESULT"]
        proxy = proxy_list[0]
        return "http://" + proxy["ip"] + ":" + proxy["port"]
    except Exception as e:
        print("get_proxy:", content)
    return None
