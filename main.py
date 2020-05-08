from PyQt5.QtWidgets import QMessageBox

import guis
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import happydb


class App:

    def __init__(self):
        self.ref = False
        pass

    def show_login(self):
        self.login = guis.Ui_login()
        self.login.show()
        self.login.login_2.clicked.connect(self.loguj)
        self.login.register_2.clicked.connect(self.rejestruj)

    def rejestruj(self):
        login, haslo, haslop, ok = guis.RegisterDialog.getLoginHaslo()
        if not ok:
            return
        if not login or not haslo or not haslop:
            self.login.label.setText("Pusty login lub hasło!")
            return
        if haslo != haslop:
            self.login.label.setText("Hasła nie są takie same!")
            return
        ok = happydb.rejestruj(login, haslo)
        if ok == None:
            self.login.label.setText("Taki użytkownik już istneje!")
            return
        if ok == False:
            self.login.label.setText("Brak połączenia z internetem!")
            return
        if ok == True:
            self.login.label.setText("Zarejestrowano!")
            return
        if ok == "Blad":
            self.login.label.setText("Za długa nazwa użytkownika!")
            return

    def loguj(self):
        login, haslo, ok = guis.LoginDialog.getLoginHaslo()
        if not ok:
            return
        if not login or not haslo:
            self.login.label.setText("Pusty login lub hasło!")
            return
        self.osoba = happydb.loguj(login, haslo)
        if self.osoba == None:
            self.login.label.setText("Hasło lub login niepoprawne!")
            return
        if self.osoba == False:
            self.login.label.setText("Brak połączenia z internetem!")
            return
        self.show_menu()

    def show_menu(self):
        self.menu = guis.Ui_menu()
        self.login.hide()
        self.menu.show()
        self.menu.setWindowTitle("Menu - "+self.osoba[1])
        self.menu.logoutBtn.clicked.connect(self.logout)
        self.menu.connectBtn.clicked.connect(self.connectRoom)
        self.menu.createBtn.clicked.connect(self.createRoom)
        self.menu.delBtn.clicked.connect(self.delRoom)
        self.menu.showBtn.clicked.connect(self.showRoom)
        self.menu.passchgBtn.clicked.connect(self.passChg)

    def connectRoom(self):
        nazwa, haslo, ok = guis.ConnectDialog.getLoginHaslo()
        if not ok:
            return
        if not nazwa or not haslo:
            self.menu.label.setText("Pusta nazwa lub hasło!")
            return
        self.room = happydb.connectRoom(nazwa, haslo)
        if self.room == None:
            self.menu.label.setText("Nieprawidłowa nazwa lub hasło!")
            return
        if self.room == False:
            self.menu.label.setText("Brak połączenia z internetem!")
            return
        self.show_chat()

    def createRoom(self):
        nazwa, haslo, haslop, ok = guis.CreateRoomDialog.getLoginHaslo()
        if not ok:
            return
        if not nazwa or not haslo or not haslop:
            self.menu.label.setText("Pusta nazwa lub hasło!")
            return
        if haslo != haslop:
            self.menu.label.setText("Hasła nie są takie same!")
            return
        ok = happydb.createRoom(nazwa, haslo, self.osoba[1])
        if ok == "Blad":
            self.menu.label.setText("Nazwa pokoju za długa!")
            return
        if ok == None:
            self.menu.label.setText("Taki pokój już istnieje!")
            return
        if ok == False:
            self.menu.label.setText("Brak połączenia z internetem!")
            return
        if ok == True:
            self.menu.label.setText("Utworzono pokój!")
            return

    def delRoom(self):
        nazwa, ok = guis.DeleteRoomDialog.getLoginHaslo()
        if not ok:
            return
        if not nazwa:
            self.menu.label.setText("Pusta nazwa!")
            return
        ok = happydb.delRoom(nazwa, self.osoba[1])
        if ok == False:
            self.menu.label.setText("Brak połączenia z internetem!")
            return
        if ok == "NotAdmin":
            self.menu.label.setText("Nie jesteś właścicelem tego pokoju!")
            return
        if ok == "NotExists":
            self.menu.label.setText("Taki pokój nie istnieje!")
            return
        if ok == True:
            self.menu.label.setText("Pomyślnie usunięto pokój.")
            return

    def showRoom(self):
        self.menu.hide()
        self.roomsMenu = guis.Ui_List()
        self.roomsMenu.show()
        self.roomsMenu.pushButton.clicked.connect(self.back)
        lista = happydb.pobierzPokoje(self.osoba[1])
        if lista == False:
            self.menu.show()
            self.roomsMenu.hide()
            self.menu.label.setText("Brak połączenia z inernetem!")
            return
        for i in range(len(lista)):
            self.roomsMenu.textBrowser.append(lista[i])
        return

    def back(self):
        self.roomsMenu.hide()
        self.menu.show()

    def passChg(self):
        haslo, haslop, ok = guis.ChangePasswordDialog.getLoginHaslo()
        if not ok:
            return
        if not haslo or not haslop:
            self.menu.label.setText("Puste hasło!")
            return
        if haslo != haslop:
            self.menu.label.setText("Hasła nie są takie same!")
            return

        ok = happydb.zmienHaslo(haslo, self.osoba[1])
        if ok == False:
            self.menu.label.setText("Brak połączenia z internetem!")
            return
        if ok == True:
            self.menu.label.setText("Zmieniono hasło!")
            return

    def logout(self):
        self.menu.hide()
        self.login.show()
        self.osoba = ""

    def show_chat(self):
        self.menu.hide()
        self.chat = guis.Ui_Chat()
        self.chat.show()
        self.chat.setWindowTitle("Chat - "+self.osoba[1]+" Pokój: "+self.room[1])
        self.chat.sendBtn.clicked.connect(self.sendMsg)
        self.chat.pushButton.clicked.connect(self.disconnectBtn)
        self.chat.lineEdit.returnPressed.connect(self.sendMsg)
        tekst = happydb.pobierzTekst(self.room[1])
        if len(tekst) > 0:
            for i in range(len(tekst)):
                self.chat.textBrowser.append(str(tekst[i][3])+": "+str(tekst[i][2]))
                self.last = tekst[i][0]
            self.ref = True
            return
        self.ref = True
        self.last = 0

    def sendMsg(self):
        self.chat.lineEdit.setReadOnly(True)
        self.ref = False
        text = self.chat.lineEdit.text()
        if text == "":
            return
        ok = happydb.sendMsg(text, self.osoba[1], self.room[1])
        if ok == False:
            self.chat.textBrowser.append("Brak połączenia z internetem!")
            return
        if ok == True:
            self.ref = True
            self.pobierzdane()
        self.chat.lineEdit.setText("")
        self.chat.lineEdit.setReadOnly(False)

    def disconnectBtn(self):
        self.chat.hide()
        self.menu.show()
        self.room = ""
        self.ref = False

    def pobierzdane(self):
        print("sek")
        if self.ref:
            print("sekk")
            self.ref = False
            tekst = happydb.pobierzTekst(self.room[1])
            if len(tekst) > 0:
                for i in range(len(tekst)):
                    if int(tekst[i][0]) > int(self.last):
                        self.chat.textBrowser.append(str(tekst[i][3]) + ": " + str(tekst[i][2]))
                        self.last = tekst[i][0]
            self.ref = True

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = App()
    controller.show_login()

    timer = QtCore.QTimer()
    timer.timeout.connect(controller.pobierzdane)
    timer.setInterval(2000)
    timer.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
