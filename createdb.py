import mysql.connector

mydb = mysql.connector.connect(
    host = "",
    user = "",
    passwd = ""
)

mycurs = mydb.cursor()

mycurs.execute("CREATE DATABASE IF NOT EXISTS hpchat_login")
mycurs.execute("CREATE DATABASE IF NOT EXISTS hpchat_rooms")

mydb_login = mysql.connector.connect(
    host = "ssh.kubaczak.com",
    user = "happy_chat",
    passwd = "pythonpass",
    database = "hpchat_login"
)

mycurs_login = mydb_login.cursor()

mycurs_login.execute("CREATE TABLE IF NOT EXISTS rooms (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), users INT, admin VARCHAR(255))")
mycurs_login.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255))")


print("Done!")