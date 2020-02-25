#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
import random
class mySQLManager:
    def __init__(self,host,user,password,database):
        """
        : param host : 连接主机地址地址
        : param user : 数据库用户名
        : param password : 用户名对应密码
        : param database ：连接的数据库
        """
        self.db = pymysql.connect(host,user,password,database )
        self.cursor = self.db.cursor()
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        # self.cursor.execute("DROP TABLE IF EXISTS fan_list")
        
        # 使用预处理语句创建表
        sql = """CREATE TABLE IF NOT EXISTS word_list (
                WORD  CHAR(100) NOT NULL,
                TRANSLATION CHAR(100)
                )DEFAULT CHARSET=utf8"""
        
        self.cursor.execute(sql)


    def add_word(self,word,translation):
        sql = "SELECT * FROM word_list \
        WHERE WORD = '%s'" % (word)
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        if  results:
            return False
        sql = """INSERT INTO word_list(WORD,TRANSLATION)
         VALUES ("{}","{}")""".format(word,translation)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("error")
            return False
        
    def ran(self):
        sql = "SELECT * FROM word_list ORDER BY rand() LIMIT 1"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results[0][0]

    def fetch(self,word):
        sql = "SELECT * FROM word_list WHERE WORD = '%s'" % word
        print(word)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)
        return result[0][1]

    def close(self):
        self.cursor.close()