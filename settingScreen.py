# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor, QPalette, QColor


class ui_settingScreen(object):
    def __init__(self):
        self.button_saveSetting = None
        self.button_main = None

    def setupUi(self, screen):
        self.setting_dialog = screen
        if screen.objectName():
            screen.setObjectName(u"dialog")
        screen.resize(800, 600)
        screen.setCursor(QCursor(Qt.ArrowCursor))
        screen.setAutoFillBackground(False)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(43, 45, 48))  # (R, G, B)
        screen.setPalette(palette)
        screen.setWindowTitle("설정 화면")

        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.label_kor = QLabel(screen)
        self.label_kor.setObjectName(u"label_kor")
        self.label_kor.setGeometry(250, 90, 300, 50)
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_kor.setFont(font1)
        self.label_kor.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_kor.setAlignment(Qt.AlignCenter)
        self.label_kor.setText("설정")

        self.line_edit = QLineEdit(screen)
        self.line_edit.setGeometry(280, 200, 240, 50)
        self.line_edit.setFont(font)


        self.button_saveSetting = QPushButton(screen)
        self.button_saveSetting.setObjectName(u"button_saveSetting")
        self.button_saveSetting.setGeometry(280, 320, 240, 80)
        self.button_saveSetting.setFont(font)
        self.button_saveSetting.setText("설정 저장")
        self.button_saveSetting.clicked.connect(self.save_setting)

        self.button_main = QPushButton(screen)
        self.button_main.setObjectName(u"button_main")
        self.button_main.setGeometry(280, 440, 240, 80)
        self.button_main.setFont(font)
        self.button_main.setText("메인으로")
        self.button_main.clicked.connect(self.return_to_main)

    def save_setting(self):
        QMessageBox.information(None, "저장 완료", "설정이 저장되었습니다.")

    def return_to_main(self):
        self.setting_dialog.hide()
