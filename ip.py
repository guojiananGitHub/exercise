import sys
from urllib import request
import json


def get_ip_information(ip):
    url = 'http://api.map.baidu.com/location/ip?ip=' + ip + '&ak=填自己的AK'
    poiss = ''
    with request.urlopen(url) as f:
        data_json = f.read()
        data_dic = json.loads(data_json)
        print(data_dic)
#   百度api已改，注釋代碼不適用
#         if data_dic():
#             content = data_dic["content"]
#             address_component = content["address_component"]
#             formatted_address = content["formatted_address"]
#             print("该IP地址的具体位置为：")
#             print(address_component["country"])
#             print(formatted_address)
#             if content.key("pois"):
#                 print("该IP地址附近POI信息如下：")
#                 pois = content["pois"]
#                 for index in range(len(pois)):
#                     pois_name = pois[index]["name"]
#                     pois_address = pois[index]["address"]
#                     print(pois_name, pois_address)
#             else:
#                 print('IP地址定位失败！！！')
if __name__ == '__main__':
    get_ip_information('填目標ip')