#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import random
import hashlib

class apiManager:
    def __init__(self, url, to, appid, secretKey):
        """
        :parasm url : api地址
        :parasm q :待翻译单词
        :parasm to:目标语言
        """
        self.u ,self.t,self.a,self.s = url,to,appid,secretKey

    def translate(self,word):
        salt = random.randint(32768, 65536)   # 生成一个随机数
        # 将appid和要翻译的字符、随机数、密钥组合成一个原始签名
        sign = self.a + word + str(salt) + self.s
        m = hashlib.new("md5")
        m.update(sign.encode(encoding="utf-8"))  # 注意使用utf-8编码
        msign = m.hexdigest()  # 得到原始签名的MD5值
        data = {
              "q": word,   
              "from": "auto",
              "to": self.t,
              "appid": self.a,
              "salt": salt,
              "sign": msign
        }
        response = requests.get(self.u,params=data)
        # 获取请求状态码 200为正常
        if(response.status_code == 200):
            # 获取相应内容
            content = response.json()
            print(content)
            return content['trans_result'][0]['dst']
            # translate_result = content["trans_result"][0]["dst"]
            # print(translate_result)
