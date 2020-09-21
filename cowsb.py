# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import gamelib
from random import random
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(0, 20, 800, 30))
        self.Heading.setObjectName("Heading")
        self.Heading.setAlignment(QtCore.Qt.AlignCenter)
        self.Heading.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.your_guess_num = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.your_guess_num.setGeometry(QtCore.QRect(300, 96, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.your_guess_num.setFont(font)
        self.your_guess_num.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.your_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.your_results.setGeometry(QtCore.QRect(300, 200, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.your_results.setFont(font)
        self.your_results.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 280, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.my_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.my_results.setGeometry(QtCore.QRect(300, 420, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.my_results.setFont(font)
        self.my_results.setObjectName("plainTextEdit_3")
        self.my_guess_num = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.my_guess_num.setGeometry(QtCore.QRect(300, 316, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.my_guess_num.setFont(font)
        self.my_guess_num.setObjectName("plainTextEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 380, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 190, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 240, 100, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.Heading.setText(_translate("MainWindow", "Cows and bulls"))
        self.label.setText(_translate("MainWindow", "Enter your guess number"))
        self.label_2.setText(_translate("MainWindow", "Your cows and bulls"))
        self.label_3.setText(_translate("MainWindow", "My guess number"))
        self.label_4.setText(_translate("MainWindow", "Enter my cows and bulls"))
        self.label_5.setText(_translate("MainWindow", "You won"))
        self.pushButton.setText(_translate("MainWindow", "Play again"))
        self.your_results.setReadOnly(True)
        self.your_guess_num.keyPressEvent = self.number_input_key
        self.my_results.keyPressEvent = self.cows_input_key
        self.pushButton.clicked.connect(self.start_game)
        self.my_guess_num.setReadOnly(True)
        self.start_game()

    def start_game(self):
        self.game_view()
        self.my_number = gamelib.start_game()
        self.your_answers = gamelib.return_full_matrix_res()
        self.my_guess = 1234
        self.cows_len = 0
        self.guess_len = 0
        self.your_guess_num.clear()
        self.my_results.clear()
        self.your_results.clear()
        self.my_guess_num.clear()
        self.your_guess_num.clear()
        self.enter_guess()
        print(self.my_number)

    def enter_cows(self):
        self.my_results.setReadOnly(False)
        self.your_guess_num.setReadOnly(True)

    def enter_guess(self):
        self.my_results.setReadOnly(True)
        self.your_guess_num.setReadOnly(False)

    def game_view(self):
        self.my_results.setVisible(True)
        self.your_results.setVisible(True)
        self.your_guess_num.setVisible(True)
        self.my_guess_num.setVisible(True)
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)
        self.label_5.setVisible(False)
        self.pushButton.setVisible(False)

    def result_view(self):
        self.my_results.setVisible(False)
        self.your_results.setVisible(False)
        self.your_guess_num.setVisible(False)
        self.my_guess_num.setVisible(False)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(True)
        self.pushButton.setVisible(True)

    def number_input_key(self, e):
        key = e.key()
        if self.guess_len != 4 and key in [Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6,
                                           Qt.Key_7, Qt.Key_8, Qt.Key_9]:
            QtWidgets.QPlainTextEdit.keyPressEvent(self.your_guess_num, e)
            self.guess_len += 1
            return
        if key == Qt.Key_Backspace:
            QtWidgets.QPlainTextEdit.keyPressEvent(self.your_guess_num, e)
            self.guess_len -= 1
            if self.guess_len < 0:
                self.guess_len = 0
            return
        if key == Qt.Key_Return:
            cows, bulls = gamelib.play_game(self.my_number,
                                            gamelib.num_to_digits(int(self.your_guess_num.toPlainText())))
            self.your_results.setPlainText(f"cows is {cows},bulls is {bulls}")
            if cows == 4:
                self.result_view()
                self.label_5.setText("you win")
            else:
                self.your_guess_num.clear()
                self.guess_len = 0
                self.enter_cows()
                self.my_guess_num.setPlainText(f"{self.my_guess}")

    def cows_input_key(self, e):
        key = e.key()
        if self.cows_len != 2 and key in [Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6,
                                          Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_0]:
            QtWidgets.QPlainTextEdit.keyPressEvent(self.my_results, e)
            self.cows_len += 1
            return
        if key == Qt.Key_Backspace:
            QtWidgets.QPlainTextEdit.keyPressEvent(self.my_results, e)
            self.cows_len -= 1
            if self.cows_len < 0:
                self.cows_len = 0
            return
        if key == Qt.Key_Return:
            print("Enrr press")
            cows_in = int(self.my_results.toPlainText())
            bulls_in = cows_in % 10
            cows_in = cows_in // 10
            self.return_guess(cows_in, bulls_in)
            print("Enrr press")
            self.my_results.clear()
            self.cows_len = 0
            self.enter_guess()

    def return_guess(self, cows_in, bulls_in):
        if cows_in == 4:
            self.result_view()
            self.label_5.setText("you loose")
            return
        i = 0
        while i < len(self.your_answers):
            cows_temp, bulls_temp = gamelib.play_game(gamelib.num_to_digits(self.your_answers[i]),
                                                      gamelib.num_to_digits(self.my_guess))
            if cows_temp != cows_in or bulls_temp != bulls_in:
                self.your_answers.remove(self.your_answers[i])
                i -= 1
            i += 1
        r = int(random() * len(self.your_answers))
        self.my_guess = self.your_answers[r]
        self.choice = 4


if __name__ == "__main__":
    import sys

    try:
        # Include in try/except block if you're also targeting Mac/Linux
        from PyQt5.QtWinExtras import QtWin

        myappid = 'newwinapps.games.cowsbulls.1.0'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Cows and bulls.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
