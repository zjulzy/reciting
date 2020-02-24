'''
@Author: your name
@Date: 2020-02-23 10:42:16
@LastEditTime: 2020-02-24 16:23:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \单词库\reciting\sql.py
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
        sql = """CREATE TABLE IF NOT EXISTS fan_list (
                WORD  CHAR(100) NOT NULL,
                ID   CHAR(20), 
                TRANSLATION CHAR(10),
                )DEFAULT CHARSET=utf8"""
        
        self.cursor.execute(sql)


    def add_word(self,info,weibo):
        """
        """
        idnum = info[1]

        sql = "SELECT * FROM fan_list \
        WHERE ID = '%s'" % (idnum)
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        if  results:
            
            return
        sql = """INSERT INTO fan_list(NAME,ID, SEX,NOTICE,FOLLOW,ADRESS,INTRODUCE,ACTIVE,WEIBOCOUNT,BIRTHDAY,STARTDATE,TAGS,BLOG,HOMEPAGE,EDUCATION,JOB,VIPLEVEL)
         VALUES ("{}","{}","{}",{},{},"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{})""".format(*info)
        print (info[:7])
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("error")
            return
        sql="""CREATE TABLE IF NOT EXISTS WEIBOLIST""" +idnum +"""(
                REPOST INT,
                COMMENT INT,
                ATTITUDE INT)DEFAULT CHARSET=utf8"""
       
        self.cursor.execute(sql)
        self.db.commit()
        for w in weibo:
            sql='''INSERT INTO WEIBOLIST'''+ idnum+'''(REPOST,COMMENT,ATTITUDE)
                    VALUES ({},{},{})'''.format(str(w[2]),str(w[1]),str(w[3]))
            # try:
            self.cursor.execute(sql)
            self.db.commit()
            # except:
            #     # 如果发生错误则回滚
            #     self.db.rollback()
            #     print("error")
    def close(self):
        self.cursor.close()