# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QPushButton, QLabel, QDialog, QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor, QPalette, QColor

from checkingScreen import ui_checkingScreen
from settingScreen import ui_settingScreen
from tetrisScreen import ui_tetrisScreen


class ui_mainScreen(object):

    def __init__(self):
        self.main_dialog = None
    def setupUi(self, screen):
        if screen.objectName():
            screen.setObjectName(u"dialog")
        screen.resize(800, 600)
        screen.setCursor(QCursor(Qt.ArrowCursor))
        screen.setAutoFillBackground(False)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(43, 45, 48))  # (R, G, B)
        screen.setPalette(palette)
        screen.setWindowTitle("시작 화면")

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
        self.label_kor.setText("테트리스 알고리즘")

        self.label_eng = QLabel(screen)
        self.label_eng.setObjectName(u"label_eng")
        self.label_eng.setGeometry(250, 140, 300, 50)
        self.label_eng.setFont(font)
        self.label_eng.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eng.setAlignment(Qt.AlignCenter)
        self.label_eng.setText("Tetris Algorithm")

        self.button_start = QPushButton(screen)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(280, 200, 240, 80)
        self.button_start.setFont(font)
        self.button_start.setCursor(QCursor(Qt.ArrowCursor))
        self.button_start.setAutoFillBackground(False)
        self.button_start.setText("테트리스 시작")
        self.button_start.clicked.connect(self.open_tetris_screen)  # button_setting 클릭 시 설정 화면 띄움


        self.button_checkRecords = QPushButton(screen)
        self.button_checkRecords.setObjectName(u"button_checkRecords")
        self.button_checkRecords.setGeometry(280, 320, 240, 80)
        self.button_checkRecords.setFont(font)
        self.button_checkRecords.setText("기록 확인")
        self.button_checkRecords.clicked.connect(self.open_records_screen)  # button_setting 클릭 시 설정 화면 띄움

        self.button_setting = QPushButton(screen)
        self.button_setting.setObjectName(u"button_setting")
        self.button_setting.setGeometry(280, 440, 240, 80)
        self.button_setting.setFont(font)
        self.button_setting.setText("세팅")
        self.button_setting.clicked.connect(self.open_setting_screen)  # button_setting 클릭 시 설정 화면 띄움

    def open_tetris_screen(self):
        tetris_Screen = QDialog()
        tetris_ui = ui_tetrisScreen()
        tetris_ui.setupUi(tetris_Screen)
        tetris_Screen.exec_()

    def open_setting_screen(self):
        # 설정 화면 생성 및 표시
        setting_Screen = QDialog()
        setting_ui = ui_settingScreen()
        setting_ui.setupUi(setting_Screen)
        setting_Screen.exec_()  # 설정 화면을 모달로 염

    def open_records_screen(self):
        recode_Screen = QDialog()
        checking_ui = ui_checkingScreen()
        checking_ui.setupUi(recode_Screen)
        recode_Screen.exec_()

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_mainScreen()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MainScreen()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()