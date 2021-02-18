import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
    database = "unapproved_vehicles",
    )



mycursor = mydb.cursor()
#alter_table = "Alter TABLE unapproved_vehicles RENAME to All_Vehicles_with_time_stamps"
sql = "DELETE FROM All_Vehicles_with_time_stamps"

mycursor.execute(sql)
#mycursor.execute(alter_table)

mydb.commit()
