#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,QMessageBox,QHBoxLayout, QVBoxLayout,QPushButton, QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui,QtCore
import baiduapi as api
import sql
import random


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        add_title = QLabel("添加新词")
        self.add_text = QLineEdit()
        add_button = QPushButton("添加")
        translate_title = QLabel("词语解释")
        translate_button = QPushButton("翻译")
        self.translate_text = QTextEdit()
        random_button = QPushButton("随机")
        self.random_word = QLineEdit()
        self.random_translation = QTextEdit()
        random_title = QLabel("随机单词")
        random_title2 = QLabel("单词释义")
        random_translate=QPushButton("翻译")
        delete_button = QPushButton("删除")
        add_panel = QGridLayout()
        random_panel = QGridLayout()
        #左部面板布局
        add_panel.setSpacing(10)
        add_panel.addWidget(add_title,1,0)
        add_panel.addWidget(self.add_text,1,1)
        add_panel.addWidget(translate_title,2,0)
        add_panel.addWidget(self.translate_text,2,1,5,1)
        add_panel.addWidget(translate_button,7,0)
        add_panel.addWidget(add_button,7,1)
        #右部面板布局
        random_panel.setSpacing(10)
        random_panel.addWidget(random_button,1,2)
        random_panel.addWidget(random_title,2,0)
        random_panel.addWidget(self.random_word,2,1,1,2)
        random_panel.addWidget(random_title2,3,0)
        random_panel.addWidget(self.random_translation,3,1,5,2)
        random_panel.addWidget(random_translate,8,1)
        random_panel.addWidget(delete_button,8,2)
        
        #全局布局
        vbox = QHBoxLayout(self)
        vbox.addLayout(add_panel)
        vbox.addLayout(random_panel)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        #绑定信号槽
        add_button.clicked.connect(self.add_keyevent)
        random_translate.clicked.connect(self.random_translate)
        translate_button.clicked.connect(self.translate_keyevent)
        random_button.clicked.connect(self.random_keyevent)
        delete_button.clicked.connect(self.delete)
        #全局界面设置
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()

        # 个人信息设置
        self.translator = api.apiManager('https://fanyi-api.baidu.com/api/trans/vip/translate','zh','20200221000386655','PwhheHAurn68ljo4NukF')
        self.mysql = sql.mySQLManager("127.0.0.1","root","60018977a","NEWWORD")

    def translate_keyevent(self):
        t = self.translator.translate(self.add_text.text())
        self.translate_text.setText(t)

    def add_keyevent(self):
        flag = self.mysql.add_word(self.add_text.text(),self.translate_text.toPlainText())
        if flag:
            msgBox = QMessageBox.about(self, u'提示', u"添加成功")

    def random_keyevent(self):
        word = self.mysql.ran()
        self.random_word.setText(word)

    def random_translate(self):
        t = self.mysql.fetch(self.random_word.text())
        self.random_translation.setText(t)

    # 删除熟悉词汇功能
    def delete(self):
        if self.random_word.text()=="":
            return 
        else:
            self.mysql.deleteWord(self.random_word.text())
            msgBox = QMessageBox.about(self, u'提示', u"删除成功")


    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mysql.close()
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
