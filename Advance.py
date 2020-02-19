# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\hp\desktop\Advance.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImagBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImagBtn.setGeometry(QtCore.QRect(20, 20, 101, 71))
        self.selectImagBtn.setObjectName("selectImagBtn")
        self.listWidget = QtWidgets.QListView(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(140, 140, 231, 91))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.selectImageLbl = QtWidgets.QLabel(self.centralwidget)
        self.selectImageLbl.setGeometry(QtCore.QRect(140, 10, 221, 121))
        self.selectImageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.selectImageLbl.setText("")
        self.selectImageLbl.setObjectName("selectImageLbl")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(20, 170, 111, 23))
        self.addBtn.setObjectName("addBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImagBtn.setText(_translate("MainWindow", "Sellect image"))
        self.addBtn.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

