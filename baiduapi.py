'''
@Author: your name
@Date: 2020-02-23 10:42:38
@LastEditTime: 2020-02-24 17:21:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \单词库\reciting\baiduapi.py
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import random
import hashlib

class apiManager:
    def __init__(self, url, q, to, appid, secretKey):
        salt = random.randint(32768, 65536)   # 生成一个随机数
        # 将appid和要翻译的字符、随机数、密钥组合成一个原始签名
        sign = appid + q + str(salt) + secretKey
        m = hashlib.new("md5")
        m.update(sign.encode(encoding="utf-8"))  # 注意使用utf-8编码
        msign = m.hexdigest()  # 得到原始签名的MD5值
        data = {
              "q": q,   
              "from": "auto",
              "to": to,
              "appid": appid,
              "salt": salt,
              "sign": msign
        }
        response = requests.get(url,params=data)
        # 获取请求状态码 200为正常
        if(response.status_code == 200):
            # 获取相应内容
            content = response.json()
            print(content)
            # translate_result = content["trans_result"][0]["dst"]
            # print(translate_result)
if __name__ =='__main__':
    demo = apiManager('https://fanyi-api.baidu.com/api/trans/vip/translate','impact','zh','20200221000386655','PwhheHAurn68ljo4NukF')
