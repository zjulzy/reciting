#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Py40 PyQt5 tutorial 
 
This program creates a statusbar.
 
author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,QHBoxLayout, QVBoxLayout,QPushButton, QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        add_title = QLabel("添加新词")
        add_text = QLineEdit()
        add_button = QPushButton("添加")
        translate_title = QLabel("词语解释")
        translate_button = QPushButton("翻译")
        translate_text = QTextEdit()
        random_button = QPushButton("随机")
        random_word = QLineEdit()
        random_translation = QTextEdit()
        random_title = QLabel("随机单词")
        random_title2 = QLabel("单词释义")
        random_translate=QPushButton("翻译")
        add_panel = QGridLayout()
        random_panel = QGridLayout()
        #左部面板布局
        add_panel.setSpacing(10)
        add_panel.addWidget(add_title,1,0)
        add_panel.addWidget(add_text,1,1)
        add_panel.addWidget(translate_title,2,0)
        add_panel.addWidget(translate_text,2,1,5,1)
        add_panel.addWidget(translate_button,7,0)
        add_panel.addWidget(add_button,7,1)
        #右部面板布局
        random_panel.setSpacing(10)
        random_panel.addWidget(random_button,1,2)
        random_panel.addWidget(random_title,2,0)
        random_panel.addWidget(random_word,2,1,1,2)
        random_panel.addWidget(random_title2,3,0)
        random_panel.addWidget(random_translation,3,1,5,2)
        random_panel.addWidget(random_translate,8,1)
        
        #全局布局
        vbox = QHBoxLayout(self)
        vbox.addLayout(add_panel)
        vbox.addLayout(random_panel)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
