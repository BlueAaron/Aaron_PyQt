#!/usr/bin/python
# -*-coding:utf-8-*-
__author__ = "Aaron"
__email__ = "876926934@qq.com"
__mtime__ = "2017/6/19 15:50"
__title__ = "带进度条启动画面"

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class CMySplashScreen(QSplashScreen):


    def __init__(self, pixmap,parent=None):
        super(CMySplashScreen, self).__init__(pixmap)


        self.ProgressBar = QProgressBar(self)
        self.ProgressBar.setGeometry(50,pixmap.height()-150,pixmap.width(),30)
        self.ProgressBar.setStyleSheet("QProgressBar {color:black;font:10px;text-align:center; }QProgressBar::chunk {background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.ProgressBar.setRange(0, 100)
        self.ProgressBar.setValue(0)
        self.ProgressBar.setTextVisible(False)
        self.ProgressBar.setFixedHeight(5)

        #窗口置顶，并且取消关闭按钮
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)

    def slotUpdateProgress(self,value):
        self.ProgressBar.setValue(value)

    #重写方法，否则点击界面就消失
    def mousePressEvent(self, QMouseEvent):
        pass

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Splash Example")
        edit = QTextEdit()
        edit.setText("Splash Example")
        self.setCentralWidget(edit)

        self.resize(600, 450)

app = QApplication(sys.argv)

splash = CMySplashScreen(QPixmap("start.jpg"))
splash.show()

splash.showMessage(u"初始化操作...", Qt.AlignLeft | Qt.AlignBottom, QColor(58, 156, 255))

for i in range(100):
    splash.slotUpdateProgress(i)
    et = QElapsedTimer()
    et.start()
    #延时操作，不能直接sleep，否则启动界面卡死
    if i ==20:
        splash.showMessage(u"正在初始化参数...", Qt.AlignLeft | Qt.AlignBottom, QColor(58, 156, 255))
        while (et.elapsed() < 100):
            app.processEvents()

    if i ==45:
        splash.showMessage(u"正在加载数据...", Qt.AlignLeft | Qt.AlignBottom, QColor(58, 156, 255))
        while (et.elapsed() < 2000):
            app.processEvents()

    if i ==90:
        splash.showMessage(u"加载成功，正在启动画面...", Qt.AlignLeft | Qt.AlignBottom, QColor(58, 156, 255))
        while (et.elapsed() < 1000):
            app.processEvents()

    while (et.elapsed() < 100):
        app.processEvents()

window = MainWindow()
window.show()
splash.finish(window)

app.exec_()



