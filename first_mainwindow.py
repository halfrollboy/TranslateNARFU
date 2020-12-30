# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 311, 371))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 60, 351, 371))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 291, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 40, 251, 20))
        self.label_2.setObjectName("label_2")
        self.words_counter = QtWidgets.QLCDNumber(self.centralwidget)
        self.words_counter.setGeometry(QtCore.QRect(330, 30, 64, 23))
        self.words_counter.setObjectName("words_counter")
        self.btn_delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_all.setGeometry(QtCore.QRect(590, 10, 141, 31))
        self.btn_delete_all.setObjectName("btn_delete_all")
        self.button_translate = QtWidgets.QPushButton(self.centralwidget)
        self.button_translate.setGeometry(QtCore.QRect(320, 440, 81, 41))
        self.button_translate.setObjectName("button_translate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_file.setGeometry(QtCore.QRect(120, 440, 151, 31))
        self.choose_file.setObjectName("choose_file")
        self.batton_save = QtWidgets.QPushButton(self.centralwidget)
        self.batton_save.setGeometry(QtCore.QRect(450, 440, 181, 31))
        self.batton_save.setObjectName("batton_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
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
        self.label.setText(_translate("MainWindow", "Введите текст для перевода"))
        self.label_2.setText(_translate("MainWindow", "Здесь появиться словарь"))
        self.btn_delete_all.setText(_translate("MainWindow", "Удалить содержимое"))
        self.button_translate.setText(_translate("MainWindow", "Первести"))
        self.label_3.setText(_translate("MainWindow", "Слов найдено в словаре"))
        self.choose_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.batton_save.setText(_translate("MainWindow", "Сохранить в файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

