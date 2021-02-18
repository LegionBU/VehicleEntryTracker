import tkinter as tk
import os
import cv2 as cv
from PIL import Image, ImageTk
import imutils
from pymysql import*
import xlwt
import pandas.io.sql as sql
import mysql.connector
import pytesseract as pyt
import keyboard
from datetime import datetime
from dateutil import tz
from zoneinfo import ZoneInfo
import export_unapproved
from export_approved import ExportApproved
from export_unapproved import ExportUnapproved

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
    database = "approved_vehicles",
    )
my_cursor = mydb.cursor()

mydb1 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
    database = "unapproved_vehicles",
    )
my_cursor1 = mydb1.cursor()



export_approved_obj = ExportApproved()
export_unapproved_obj = ExportUnapproved()

class UnapprovedDatabase():
  def __init__(self):
    self.mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
    database = "unapproved_vehicles",
    )
    self.my_cursor = self.mydb.cursor()
  def add_to_vehicles_with_timestamps(self, num):
    dtobj = datetime.now()
    time = dtobj.strftime("%d/%m/%Y, %H:%M:%S")
    #my_cursor1.execute("CREATE TABLE unapproved_vehicles (License_plate_num VARCHAR(255), Time_of_Entry VARCHAR(255))")
    sql_stuff = "INSERT INTO All_Vehicles_with_time_stamps (License_plate_num, Time_of_Entry) VALUES (%s, %s)"
    records1 = (num, time)
    self.my_cursor.execute(sql_stuff, records1)
    self.mydb.commit()

unapproved_db = UnapprovedDatabase()
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password123",
            database = "approved_vehicles",
            )

        self.my_cursor = self.mydb.cursor()

        self.records = [('Kamala Rajan', 'UP24AX8793'),
            ('Karanjit Aulakh', 'PB44ES1234'),
            ('Suyash Matanhelia', 'UP32H06262'),
            ('Aruna Ganguly', 'UP24HF8234'),
            ('Saumil Sood', 'HR20AB8008'),
            ('Arishmit Ghosh', 'WB06G8224'),
            ('Tanmay Singh', 'TN14AS3127'),
            ('Siddhant Nigam', 'KA03MX5058'),
            ('Farhan Ahmed', 'UP24AB2244'),
            ('Anthony Smith', 'UP24CZ1678')
        ]
        self.con=connect(user="root",password="password123",host="localhost",database="approved_vehicles")
        self.df=sql.read_sql('select * from approved_vehicles', self.con)

    def exec(self, num):
        self.my_cursor.execute("SELECT * FROM approved_vehicles")
        result = self.my_cursor.fetchall()
        for tup in result:
            if tup[1] == num:
                return("The vehicle is already a registered approved vehicle and belongs to {}".format(tup[0]))
        return ('No vehicle found')

    def exportDbApproved(self):
        self.df.to_excel('authorised.xlsx')

    '''mydb1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password123",
        )
    my_cursor1 = mydb1.cursor()'''

    #my_cursor1.execute("CREATE DATABASE unapproved_vehicles")
    #my_cursor1.execute("CREATE TABLE unapproved_vehicles (License_plate_num VARCHAR(255))")

    #table_info = "INSERT INTO unapproved_vehicles (License_plate_num) VALUES (%s)"
pyt.pytesseract.tesseract_cmd = r'C://Program Files/Tesseract-OCR/tesseract'
db = Database()

window = tk.Tk()
window.configure(background='gray')
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff = 0)

file_menu.add_command(label = "Help")
file_menu.add_command(label = "Start")
file_menu.add_command(label="Exit", command= window.quit)

edit_menu = tk.Menu(menubar, tearoff = 0)
edit_menu.add_command(label = "Export Database", command = db.exportDbApproved)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
window.config(menu = menubar)

load = cv.imread("C:\\Users\Saumil\Desktop\Project_Files\photocar.png")
load = cv.resize(load, (800, 600))
load = cv.cvtColor(load, cv.COLOR_BGR2RGBA)
load = Image.fromarray(load)
photo = ImageTk.PhotoImage(load)

video_label = tk.Label(window, image = photo, height = 600, width = 800)
video_label.pack(side = tk.LEFT, padx = 2, pady = 2, expand = 0)

text_label = tk.Label(window, text = "Current Vehicle Number: ",font=("Times New Roman", 14), justify = tk.LEFT)
text_label.pack(padx = 2, pady = 2)

vehicle_number_text = tk.Label(window, text = "<Number To Be Displayed Here>", font=("Century", 12), relief = "raised")
vehicle_number_text.pack(padx = 2 , pady = 20)

vehicle_number_response = tk.Label(window, text = "<Number To Be Displayed Here>", font=("Century", 12))
vehicle_number_response.pack(padx = 2 , pady = 20)


video_input = cv.VideoCapture(0)

def extractText(p):
    predicted_result = pyt.image_to_string(p, lang ='eng')
    filter_predicted_result = "".join(predicted_result.split()).replace('\\','').replace('/','').replace('~','').replace('!', '').replace(":", "").replace('%', '').replace('#', '').replace("-", "").replace('“', '').replace('@', '').replace('‘', '').replace(')', '').replace('(', '').replace('|', '').replace('.', '')
    return filter_predicted_result

global isButtonDisplayed
isButtonDisplayed = False
def start_video():
    check, frame = video_input.read()
    if check == True:
        if keyboard.is_pressed('f'):
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            image = frame.copy()
            image = imutils.resize(image, width=500)
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            gray = cv.bilateralFilter(gray, 11, 17, 17)
            edged = cv.Canny(gray, 170, 200)
            cv.imshow("Edges", edged)
            (cnts, _) = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            cnts=sorted(cnts, key = cv.contourArea, reverse = True)[:30]
            NumberPlateCnt = None
            count = 0
            for c in cnts:
                peri = cv.arcLength(c, True)
                approx = cv.approxPolyDP(c, 0.02 * peri, True)
                if len(approx) == 4:  # Select the contour with 4 corners
                    area = cv.contourArea(approx)
                    if area > 500 and area < 3000:
                        print(area)
                        NumberPlateCnt = approx #This is our approx Number Plate Contour
                        x, y, w, h = cv.boundingRect(approx)
                        plate = image[y:y+h, x:x+w]
                        cv.imshow("Plate", plate)
                        num = extractText(plate)
                        print(num)
                        vehicle_number_text.text = num
                        vehicle_number_text.config(text = num)
                        response = db.exec(num)
                        vehicle_number_response.text = response
                        vehicle_number_response.config(text = response)
                        unapproved_db.add_to_vehicles_with_timestamps(num)
                        break
        frame = cv.resize(frame, (800, 600))
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        video_label.image = frame
        video_label.config(image = frame)
        video_label.after(10, start_video)

exprt_apprvd_btn = tk.Button(window, bg = "blue", fg = "white", width = 20, height = 2, text = "Export Excel Approved", command = export_approved_obj.export_approved)
exprt_apprvd_btn.pack(padx = 4, pady = 12)
exprt_unapprovd_btn = tk.Button(window, bg = "blue", fg = "white", width = 20, height = 2, text = "Export Excel Unapproved", command = export_unapproved_obj.export_unapproved)
exprt_unapprovd_btn.pack(padx = 4, pady = 12)
Start_btn = tk.Button(window, bg = "red", fg = "white", width = 20, height = 2, text = "Start", command = start_video)
Start_btn.pack(side = tk.BOTTOM, padx = 2, pady = 10)

window.geometry("1920x1080")
window.mainloop()
