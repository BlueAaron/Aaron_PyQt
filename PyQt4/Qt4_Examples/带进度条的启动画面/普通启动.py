#!/usr/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

'''
缺点：
1.点击画面消失，点击画面外，画面消失，不能固定
2.阻塞主界面，点击启动画面卡死
'''

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Splash Example")
        edit = QTextEdit()
        edit.setText("Splash Example")
        self.setCentralWidget(edit)

        self.resize(600, 450)

        QThread.sleep(3)


app = QApplication(sys.argv)

splash = QSplashScreen(QPixmap("start.jpg"))
splash.show()
app.processEvents()
window = MainWindow()
window.show()
splash.finish(window)

app.exec_()
