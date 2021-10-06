from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import enterWindow
import sqlite3


class Ui_AdminWindow(QMainWindow):
    def __init__(self):
        super(Ui_AdminWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.setWindowTitle("Лабараторная №1")
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(270, 50)
        self.label.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                 "color: rgb(255, 179, 134);")
        self.label.setObjectName("label")
        self.label.setFixedWidth(300)

        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(255, 100, 300, 40))
        self.Login.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                 "background-color: rgb(240, 217, 185);")
        self.Login.setObjectName("Login")

        self.Registration_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Registration_Button.setGeometry(QtCore.QRect(330, 160, 150, 40))
        self.Registration_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Registration_Button.setMouseTracking(True)
        self.Registration_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                               "background-color: rgb(162, 73, 0);")
        self.Registration_Button.setObjectName("Registration_Button")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setGeometry(QtCore.QRect(255, 220, 300, 40))
        self.Password.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                    "background-color: rgb(240, 217, 185);")
        self.Password.setObjectName("Password")

        self.Password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_2.setGeometry(QtCore.QRect(255, 280, 300, 40))
        self.Password_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                      "background-color: rgb(240, 217, 185);")
        self.Password_2.setObjectName("Password_2")

        self.Conf_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Conf_Button.setGeometry(QtCore.QRect(330, 340, 150, 40))
        self.Conf_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conf_Button.setMouseTracking(True)
        self.Conf_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Conf_Button.setObjectName("Conf_Button")

        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.move(50, 390)
        self.User.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                "color: rgb(255, 179, 134);")
        self.User.setObjectName("User")
        self.User.setFixedWidth(500)

        self.Ban = QtWidgets.QCheckBox(self.centralwidget)
        self.Ban.move(300, 390)
        self.Ban.setStyleSheet("""QCheckBox::indicator {width: 40px; height: 40px;}""")

        self.Ban_Text = QtWidgets.QLabel(self.centralwidget)
        self.Ban_Text.move(340, 400)
        self.Ban_Text.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                    "color: rgb(255, 179, 134);")
        self.Ban_Text.setObjectName("Ban_Text")
        self.Ban_Text.setFixedWidth(100)

        self.Limit = QtWidgets.QCheckBox(self.centralwidget)
        self.Limit.move(500, 390)
        self.Limit.setStyleSheet("""QCheckBox::indicator {width: 40px; height: 40px;}""")

        self.Limit_Text = QtWidgets.QLabel(self.centralwidget)
        self.Limit_Text.move(540, 400)
        self.Limit_Text.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                      "color: rgb(255, 179, 134);")
        self.Limit_Text.setObjectName("Limit_Text")
        self.Limit_Text.setFixedWidth(250)

        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_Button.setGeometry(QtCore.QRect(430, 430, 150, 40))
        self.Next_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_Button.setMouseTracking(True)
        self.Next_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Next_Button.setObjectName("Next_Button")

        self.Prev_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Prev_Button.setGeometry(QtCore.QRect(230, 430, 150, 40))
        self.Prev_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_Button.setMouseTracking(True)
        self.Prev_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Prev_Button.setObjectName("Prev_Button")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(330, 540, 150, 40))
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setMouseTracking(True)
        self.Exit_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Exit_Button.setObjectName("Exit_Button")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstUser()
        self.addFunctionsClick()
        self.nowUserID = 1

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Панель администратора"))
        self.Login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.Registration_Button.setText(_translate("MainWindow", "Создать"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Новый пароль"))
        self.Password_2.setPlaceholderText(_translate("MainWindow", "Повторите пароль"))
        self.Conf_Button.setText(_translate("MainWindow", "Подтвердить"))
        self.Exit_Button.setText(_translate("MainWindow", "Выход"))
        self.Next_Button.setText(_translate("MainWindow", "Следующий"))
        self.Prev_Button.setText(_translate("MainWindow", "Предыдущий"))
        self.Ban_Text.setText(_translate("MainWindow", "Забанить"))
        self.Limit_Text.setText(_translate("MainWindow", "Установить ограничения"))

    def addFunctionsClick(self):
        self.Registration_Button.clicked.connect(lambda: self.registration(self.Login.text()))
        self.Conf_Button.clicked.connect(lambda: self.change(self.Password.text(), self.Password_2.text()))
        self.Next_Button.clicked.connect(lambda: self.nextUser())
        self.Prev_Button.clicked.connect(lambda: self.prevUser())
        self.Exit_Button.clicked.connect(lambda: self.exit())
        self.Ban.stateChanged.connect(lambda: self.ban())
        self.Limit.stateChanged.connect(lambda: self.limit())

    def registration(self, Login):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users(ID INT, Login TEXT, Password TEXT, Banned INT, Limited INT)")
        cur.execute("SELECT Login FROM Users")
        LoginDB = str(cur.fetchall())
        cur.execute("SELECT ID FROM Users")
        ID = cur.fetchall()[::-1]
        banned = 0
        limited = 0
        if Login not in LoginDB and Login != "":
            cur.execute(f"INSERT INTO Users(ID, Login, Password, Banned, Limited) VALUES (?, ?, ?, ?, ?)",
                        (ID[0][0] + 1, Login, "", banned, limited))
            db.commit()
        cur.close()
        db.close()
        self.Login.setText("")

    def change(self, Password, PasswordConf):
        if Password != "" and Password == PasswordConf:
            db = sqlite3.connect("database.db")
            cur = db.cursor()
            cur.execute("UPDATE Users SET Password = ? WHERE Login = ?", (Password, "ADMIN"))
            db.commit()
            cur.close()
            db.close()
            self.Password.setText("")
            self.Password_2.setText("")

    def firstUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        cur.execute("SELECT Login FROM Users WHERE ID = ?", (1,))
        Login = cur.fetchall()

        cur.execute("SELECT Banned FROM Users WHERE ID = ?", (1,))
        banned = cur.fetchall()

        cur.execute("SELECT Limited FROM Users WHERE ID = ?", (1,))
        limited = cur.fetchall()

        cur.close()
        db.close()

        self.User.setText(Login[0][0])
        if banned[0][0] == 1:
            self.Ban.setChecked(True)
        else:
            self.Ban.setChecked(False)

        if limited[0][0] == 1:
            self.Limit.setChecked(True)
        else:
            self.Limit.setChecked(False)

    def ban(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.Ban.isChecked():
            cur.execute("UPDATE Users SET Banned = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Banned = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        if self.Limit.isChecked():
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        cur.close()
        db.close()

    def limit(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.Limit.isChecked():
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        cur.close()
        db.close()

    def nextUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("SELECT ID FROM Users")
        ID = cur.fetchall()[::-1]

        if self.nowUserID + 1 <= ID[0][0]:
            cur.execute("SELECT Login FROM Users WHERE ID = ?", (self.nowUserID + 1,))
            Login = cur.fetchall()

            self.User.setText(Login[0][0])
            self.nowUserID += 1

            cur.execute("SELECT Banned FROM Users WHERE ID = ?", (self.nowUserID,))
            banned = cur.fetchall()

            cur.execute("SELECT Limited FROM Users WHERE ID = ?", (self.nowUserID,))
            limited = cur.fetchall()

            cur.close()
            db.close()

            if banned[0][0] == 1:
                self.Ban.setChecked(True)
            else:
                self.Ban.setChecked(False)

            if limited[0][0] == 1:
                self.Limit.setChecked(True)
            else:
                self.Limit.setChecked(False)

    def prevUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.nowUserID - 1 > 0:
            cur.execute("SELECT Login FROM Users WHERE ID = ?", (self.nowUserID - 1,))
            Login = cur.fetchall()

            self.User.setText(Login[0][0])
            self.nowUserID -= 1

            cur.execute("SELECT Banned FROM Users WHERE ID = ?", (self.nowUserID,))
            banned = cur.fetchall()

            cur.execute("SELECT Limited FROM Users WHERE ID = ?", (self.nowUserID,))
            limited = cur.fetchall()

            cur.close()
            db.close()

            if banned[0][0] == 1:
                self.Ban.setChecked(True)
            else:
                self.Ban.setChecked(False)

            if limited[0][0] == 1:
                self.Limit.setChecked(True)
            else:
                self.Limit.setChecked(False)

    def exit(self):
        EnterW = enterWindow.Ui_EnterWindow()
        EnterW.show()
        self.close()