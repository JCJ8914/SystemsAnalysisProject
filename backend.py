from distutils.util import execute
import sqlite3

def clientData():
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS client_data (id INTEGER AUTO_INCREMENT PRIMARY KEY, CusNo text, CusFirstName text, CusLastName text, CusContact text, CusAddress text, CusRoom text, CusInDate text, CusOutDate text)")
    communication.commit()
    communication.close()

def addData(CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("INSERT INTO client_data (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    communication.commit()
    communication.close()

def viewData():
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("SELECT * FROM client_data")

    rows = cur.fetchall
    communication.close
    return rows

def deleteData(id):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("DELETE FROM client_data WHERE CusNo = ?", (id,))

    rows = cur.fetchall
    communication.close
    return rows

def searchData(ID="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("SELECT * FROM client_data WHERE CusFirstName=? OR CusLastName=? OR CusContact=? OR CusAddress=? OR CusRoom=? OR CusInDate? OR CusOutDate=?", (CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    rows = cur.fetchall
    communication.close
    return rows

def updateData(ID="", CusID="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("UPDATE client_data SET CusID="" CusFirstName=?, CusLastName=?, CusContact=?, CusAddress=?, CusRoom=?, CusInDate=?, CusOutDate=?", (CusID, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    communication.commit()
    communication.close()

clientData()