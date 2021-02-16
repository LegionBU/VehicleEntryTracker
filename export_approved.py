from pymysql import*
import xlwt
import pandas.io.sql as sql

class ExportApproved():
    def __init__(self):
        self.con=connect(user="root",password="password123",host="localhost",database="approved_vehicles")
        self.df=sql.read_sql('select * from approved_vehicles', self.con)

    def export_approved(self):
        self.df.to_excel('approved_vehicles.xlsx')
