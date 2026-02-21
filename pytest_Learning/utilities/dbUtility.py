import mysql.connector

def db_Connection():
    global mysql
    mysql = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="pydb"
    )

def getresult(query):
    mycursor = mysql.cursor()
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result