from pymysql import*
import xlwt
import pandas.io.sql as sql
class ExportUnapproved():
    def __init__(self):
        self.con=connect(user="root",password="password123",host="localhost",database="unapproved_vehicles")
        self.df=sql.read_sql('select * from unapproved_vehicles', self.con)
    def export_unapproved(self):
        self.df.to_excel('unapproved_vehicles.xlsx')
