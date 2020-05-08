"""try:
    f = open("config.py")
    f.close()
except:
    f = open("config.py", "w")
    f.write(mysql = {
    "host": "localhost",
    "user": "root",
    "passwd": "my secret password"
}
    )"""

import mysql.connector
import hashlib

try:
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        passwd = ""
    )
except:
    print("Brak połączenia z internetem, lub baza danych nie istnieje! Uzupełnij config.py")

def bazacl(output):
    x = output
    t = []
    for i in x:
        z = str(i)
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace(",", "")
        z = z.replace("'", "")
        t.append(z)
    t = t[0].split(sep=" ")
    return t

def bazaclmsg(output):
    x = output
    t = []
    for i in range(len(x)):
        z = str(x[i])
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace("'", "")
        f = z.split(sep=", ")
        t.append(f)
    return t

def bazaclroom(output):
    t = []
    for i in range(len(output)):
        z = str(output[i])
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace("'", "")
        z = z.replace(",", "")
        t.append(z)
    return t

def loguj(login, haslo):
    try:
        log = login.replace(" ", "_")
        passw = hashlib.sha256(haslo.encode('utf-8')).hexdigest()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM hpchat_login.users WHERE name = '"+log+"' AND password = '"+passw+"';")
        out = mycursor.fetchall()
        if len(out) == 0:
            return None
        out = bazacl(out)
        return out
    except:
        return False

def rejestruj(login, haslo):
    try:
        log = login.replace(" ", "_")
        if len(log) > 64:
            return "Blad"
        passw = hashlib.sha256(haslo.encode('utf-8')).hexdigest()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM hpchat_login.users WHERE name = '"+log+"';")
        out = mycursor.fetchall()
        if len(out) != 0:
            return None
        else:
            sql = "INSERT INTO hpchat_login.users (name, password) VALUES (%s, %s)"
            var = (log, passw)
            mycursor.execute(sql, var)
            mydb.commit()
            return True
    except:
        return False

def connectRoom(nazwa, haslo):
    try:
        name = nazwa.replace(" ", "_")
        passw = hashlib.sha256(haslo.encode('utf-8')).hexdigest()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM hpchat_login.rooms WHERE name = '"+name+"' AND password = '"+passw+"';")
        out = mycursor.fetchall()
        if len(out) == 0:
            return None
        out = bazacl(out)
        return out
    except:
        return False

def pobierzTekst(room):
    try:
        mydb.connect()
        mycursor = mydb.cursor()
        pokoj = "hpchat_rooms."+str(room)
        mycursor.execute("SELECT * FROM "+pokoj+";")
        out = mycursor.fetchall()
        out = bazaclmsg(out)
        return out
    except:
        print("Blad")
        return False

def createRoom(nazwa, haslo, admin):
    try:
        log = nazwa.replace(" ", "_")
        if len(log) > 64:
            return "Blad"
        passw = hashlib.sha256(haslo.encode('utf-8')).hexdigest()
        mycursor = mydb.cursor()
        nazwa = log
        log = "hpchat_rooms."+str(log)
        try:
            mycursor.execute("SELECT * FROM "+log+";")
            return None
        except:
            mycursor.execute("CREATE TABLE "+log+" (id INT AUTO_INCREMENT PRIMARY KEY, czas VARCHAR(255), message VARCHAR(255), user VARCHAR(255))")
            mydb.commit()
            sql = "INSERT INTO hpchat_login.rooms (name, password, users, admin) VALUES (%s, %s, %s, %s)"
            var = (nazwa, passw, 0, admin)
            mycursor.execute(sql, var)
            mydb.commit()
            return True
    except:
        return False

def delRoom(nazwa, admin):
    try:
        nazwa = nazwa.replace(" ", "_")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM hpchat_login.rooms WHERE name = '"+nazwa+"';")
        out = mycursor.fetchall()
        if len(out) != 0:
            out = bazacl(out)
            if out[4] == admin:
                mycursor.execute("DELETE FROM hpchat_login.rooms WHERE name = '"+nazwa+"';")
                mydb.commit()
                nazwa = "hpchat_rooms."+nazwa
                mycursor.execute("DROP TABLE "+nazwa+";")
                mydb.commit()
                return True
            else:
                return "NotAdmin"
        else:
            return "NotExists"
    except:
        return False

def pobierzPokoje(osoba):
    try:
        osoba = osoba.replace(" ", "_")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name FROM hpchat_login.rooms WHERE admin = '"+osoba+"';")
        out = mycursor.fetchall()
        out = bazaclroom(out)
        return out
    except:
        return False

def zmienHaslo(haslo, login):
    try:
        login = login.replace(" ", "_")
        passw = hashlib.sha256(haslo.encode('utf-8')).hexdigest()
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE hpchat_login.users SET password = '"+passw+"' WHERE name = '"+login+"';")
        mydb.commit()
        return True
    except:
        return False

def sendMsg(msg, osoba, pokoj):
    try:
        pokoj = "hpchat_rooms."+pokoj
        sql = "INSERT INTO "+pokoj+" (czas, message, user) VALUES (%s, %s, %s);"
        val = ("now", msg, osoba)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    except:
        return False