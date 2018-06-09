import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import BotAccount
from selenium.webdriver.common.keys import Keys

# IP 우회 접속
"""
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='/Users/paramount/Downloads/phantomjs/bin/phantomjs', service_args=service_args)

driver.get('https://www.supremenewyork.com/shop')

driver.save_screenshot('search_results.png')
"""

form_class = uic.loadUiType("SuperSupreme.ui")[0]

class QtDesigner(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.lineEdit.textChanged.connect(self.account_changed)
        self.lineEdit_2.textChanged.connect(self.account_changed_2)
        self.lineEdit_3.textChanged.connect(self.account_changed_3)
        self.lineEdit_4.textChanged.connect(self.account_changed_4)
        self.lineEdit_5.textChanged.connect(self.account_changed_5)
        self.lineEdit_6.textChanged.connect(self.account_changed_6)
        self.lineEdit_7.textChanged.connect(self.account_changed_7)
        self.lineEdit_8.textChanged.connect(self.account_changed_8)
        self.lineEdit_9.textChanged.connect(self.account_changed_9)
        self.lineEdit_10.textChanged.connect(self.account_changed_10)
        self.lineEdit_11.textChanged.connect(self.account_changed_11)
        self.lineEdit_12.textChanged.connect(self.account_changed_12)
        self.pushButton.clicked.connect(self.check)

    # 현재 시간 표시
    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "Current Time : " + text_time
        self.statusbar.showMessage(time_msg)

    # 텍스트 자동 완성
    def account_changed(self, info):
        self.info = self.lineEdit.text()
    def account_changed_2(self, info_2):
        self.info_2 = self.lineEdit_2.text()
    def account_changed_3(self, info_3):
        self.info_3 = self.lineEdit_3.text()
    def account_changed_4(self, info_4):
        self.info_4 = self.lineEdit_4.text()
    def account_changed_5(self, info_5):
        self.info_5 = self.lineEdit_5.text()
    def account_changed_6(self, info_6):
        self.info_6 = self.lineEdit_6.text()
    def account_changed_7(self, info_7):
        self.info_7 = self.lineEdit_7.text()
    def account_changed_8(self, info_8):
        self.info_8 = self.lineEdit_8.text()
    def account_changed_9(self, info_9):
        self.info_9 = self.lineEdit_9.text()
    def account_changed_10(self, info_10):
        self.info_10 = self.lineEdit_10.text()
    def account_changed_11(self, info_11):
        self.info_11 = self.lineEdit_11.text()
    def account_changed_12(self, info_12):
        self.info_12 = self.lineEdit_12.text()

    # Check 버튼 클릭
    def check(self):
        driver = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        driver.get('https://okky.kr/user/register')

        assert 'OKKY' in driver.title

        input_element = driver.find_element_by_name('username')
        input_element.send_keys(self.info)

        input_element = driver.find_element_by_name('password')
        input_element.send_keys(self.info_2)

        input_element = driver.find_element_by_name('person.email')
        input_element.send_keys(self.info_3)

        input_element = driver.find_element_by_name('person.fullName')
        input_element.send_keys(self.info_4)

        input_element = driver.find_element_by_name('avatar.nickname')
        input_element.send_keys(self.info_5)

        driver.save_screenshot('search_results.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtDesigner = QtDesigner()
    QtDesigner.show()
    app.exec_()
