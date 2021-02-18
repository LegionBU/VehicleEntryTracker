import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password123",
  database="approved_vehicles"
)

mycursor = mydb.cursor()

sql = "UPDATE approved_vehicles SET License_plate_num = %s WHERE Owner_Name = %s"
val = ("MH14GY9216", "Saumil Sood")

mycursor.execute(sql, val)

mydb.commit()
