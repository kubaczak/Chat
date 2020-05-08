from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QDialogButtonBox, QGridLayout


class Ui_login(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("login")
        self.resize(300, 100)
        self.setFixedSize(300, 100)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.login_2.setObjectName("login_2")
        self.horizontalLayout.addWidget(self.login_2)
        self.register_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.register_2.setObjectName("register_2")
        self.horizontalLayout.addWidget(self.register_2)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(26, 72, 241, 21))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("login", "Zaloguj"))
        self.login_2.setText(_translate("login", "Zaloguj"))
        self.register_2.setText(_translate("login", "Utwórz Konto"))


class Ui_menu(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("menu")
        self.resize(400, 121)
        self.setFixedSize(400, 141)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(15, 0, 15, 0)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.connectBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout.addWidget(self.connectBtn, 0, 0, 1, 1)
        self.createBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.createBtn.setObjectName("createBtn")
        self.gridLayout.addWidget(self.createBtn, 0, 1, 1, 1)
        self.delBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 1, 1, 1, 1)
        self.passchgBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.passchgBtn.setObjectName("passchgBtn")
        self.gridLayout.addWidget(self.passchgBtn, 1, 0, 1, 1)
        self.showBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.showBtn.setObjectName("showBtn")
        self.gridLayout.addWidget(self.showBtn, 0, 2, 1, 1)
        self.logoutBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logoutBtn.setObjectName("logoutBtn")
        self.gridLayout.addWidget(self.logoutBtn, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(6, 120, 391, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("menu", "Menu"))
        self.connectBtn.setText(_translate("menu", "Połącz z pokojem"))
        self.createBtn.setText(_translate("menu", "Utwórz pokój"))
        self.delBtn.setText(_translate("menu", "Usuń pokój"))
        self.passchgBtn.setText(_translate("menu", "Zmień hasło"))
        self.showBtn.setText(_translate("menu", "Pokaż twoje pokoje"))
        self.logoutBtn.setText(_translate("menu", "Wyloguj"))


class Ui_Chat(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Chat")
        self.resize(500, 600)
        self.setFixedSize(500, 600)
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 471, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 510, 461, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.sendBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout.addWidget(self.sendBtn)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 560, 141, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(210, 550, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Chat", "HappyChat"))
        self.sendBtn.setText(_translate("Chat", "Wyślij"))
        self.label.setText(_translate("Chat", ""))
        self.pushButton.setText(_translate("Chat", "Rozłącz"))

class Ui_List(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Dialog")
        self.resize(300, 500)
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 281, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 450, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Twoje pokoje"))
        self.pushButton.setText(_translate("Dialog", "Powrót"))


class LoginDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Login')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Logowanie')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo = dialog.loginHaslo()
        return (login, haslo, ok == QDialog.Accepted)

class RegisterDialog(QDialog):
    """ Okno dialogowe rejestracji """
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Login')
        hasloLbl = QLabel('Hasło')
        haslopLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslop = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)
        self.haslop.setEchoMode(QLineEdit.Password)
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(haslopLbl, 2, 0)
        uklad.addWidget(self.haslop, 2, 1)
        uklad.addWidget(self.przyciski, 3, 0, 3, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Rejestracja')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip(),
                self.haslop.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = RegisterDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo, haslop = dialog.loginHaslo()
        return (login, haslo, haslop, ok == QDialog.Accepted)

class ConnectDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Nazwa')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Połącz z Pokojem')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = ConnectDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo = dialog.loginHaslo()
        return (login, haslo, ok == QDialog.Accepted)

class CreateRoomDialog(QDialog):
    """ Okno dialogowe rejestracji """
    def __init__(self, parent=None):
        super(CreateRoomDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Nazwa')
        hasloLbl = QLabel('Hasło')
        haslopLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslop = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)
        self.haslop.setEchoMode(QLineEdit.Password)
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(haslopLbl, 2, 0)
        uklad.addWidget(self.haslop, 2, 1)
        uklad.addWidget(self.przyciski, 3, 0, 3, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Utwórz pokój')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip(),
                self.haslop.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = CreateRoomDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo, haslop = dialog.loginHaslo()
        return (login, haslo, haslop, ok == QDialog.Accepted)

class DeleteRoomDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(DeleteRoomDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Nazwa')
        self.login = QLineEdit()
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Usuń pokój')

    def loginHaslo(self):
        return (self.login.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = DeleteRoomDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login = dialog.loginHaslo()
        return (login, ok == QDialog.Accepted)

class ChangePasswordDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(ChangePasswordDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Hasło')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)
        self.login.setEchoMode(QLineEdit.Password)
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Zmień hasło')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = ChangePasswordDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo = dialog.loginHaslo()
        return (login, haslo, ok == QDialog.Accepted)