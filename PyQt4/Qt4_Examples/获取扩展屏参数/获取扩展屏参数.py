#!/usr/bin/python
# -*-coding:utf-8-*-
__author__ = "Aaron"
__email__ = "876926934@qq.com"
__mtime__ = "2017-03-30 13:48"
__title__ = "扩展屏"

import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('center')
        self.resize(250, 150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

app = QtGui.QApplication(sys.argv)
desktop = app.desktop()
#获取主屏幕的索引序号，（windows开始菜单所在的屏幕为主屏幕）， 每个副屏幕序号+1
print u"主屏幕的索引序号",desktop.primaryScreen()
#获取当前屏幕个数
print u"当前屏幕个数",desktop.screenCount()
#根据当前的屏幕序号获取屏幕宽高等属性
print desktop.screenGeometry(0)

qb = Center()
qb.show()
sys.exit(app.exec_())