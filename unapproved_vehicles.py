from datetime import datetime
from dateutil import tz
from zoneinfo import ZoneInfo
import mysql.connector

class AddUnapproved():
	def __init__(self):
		self.mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			passwd = "password123",
			database = "unapproved_vehicles",
			)
		self.my_cursor = self.mydb.cursor()
	def add_to_unapproved(self, num):
		dtobj = datetime.now()
		time = dtobj.strftime("%d/%m/%Y, %H:%M:%S")
		#my_cursor1.execute("CREATE TABLE unapproved_vehicles (License_plate_num VARCHAR(255), Time_of_Entry VARCHAR(255))")
		sql_stuff = "INSERT INTO unapproved_vehicles (License_plate_num, Time_of_Entry) VALUES (%s, %s)"
		records1 = (num, time)
		self.my_cursor.execute(sql_stuff, records1)
		self.mydb.commit()
