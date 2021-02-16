
import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "password123",
	database = "approved_vehicles",
	)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE approved_vehicles")

#my_cursor.execute("CREATE TABLE approved_vehicles (Owner_Name VARCHAR(255), License_plate_num VARCHAR(255))")
#table_info = "INSERT INTO approved_vehicles (Owner_Name, License_plate_num) VALUES (%s, %s)"
'''records = [('Kamala Rajan', 'UP24AX8793'),
	('Karanjit Aulakh', 'PB44ES1234'),
	('Suyash Matanhelia', 'UP32HD6262'),
	('Aruna Ganguly', 'UP24HF8234'),
	('Saumil Sood', 'HR20AB8008'),
	('Arishmit Ghosh', 'WB06G8224'),
	('Tanmay Singh', 'TN14AS3127'),
	('Siddhant Nigam', 'KA03MX5058'),
	('Farhan Ahmed', 'UP24AB2244'),
	('Anthony Smith', 'UP24CZ1678')
]'''
#my_cursor.executemany(table_info, records)
#mydb.commit()

#my_cursor.execute("SELECT * FROM approved_vehicles")
#result = my_cursor.fetchall()
#print(result)
#for tup in result:
	#if tup[1] == a:
	#	print("The vehicle is already a registered approved vehicle and belongs to {}".format(tup[0]))
	#	break
