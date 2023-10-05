# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor, QPalette, QColor


class ui_tetrisScreen(object):
    def __init__(self):
        self.set_screen = None
        self.button_saveSetting = None
        self.button_main = None

    def setupUi(self, screen):
        if screen.objectName():
            screen.setObjectName(u"dialog")
        screen.resize(800, 600)
        screen.setCursor(QCursor(Qt.ArrowCursor))
        screen.setAutoFillBackground(False)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(43, 45, 48))  # (R, G, B)
        screen.setPalette(palette)
        screen.setWindowTitle("테트리스 화면")

        self.label_kor = QLabel(screen)
        self.label_kor.setObjectName(u"label_kor")
        self.label_kor.setGeometry(250, 30, 300, 50)
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_kor.setFont(font1)
        self.label_kor.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_kor.setAlignment(Qt.AlignCenter)
        self.label_kor.setText("테트리스")


        # self.button_main = QPushButton(screen)
        # self.button_main.setObjectName(u"button_main")
        # self.button_main.setGeometry(280, 440, 240, 80)
        # self.button_main.setFont(font)
        # self.button_main.setText("메인으로")
