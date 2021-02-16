import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
    database = "unapproved_vehicles",
    )



mycursor = mydb.cursor()

sql = "DELETE FROM unapproved_vehicles"

mycursor.execute(sql)

mydb.commit()
