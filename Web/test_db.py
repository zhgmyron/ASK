__author__ = 'rzhao'
import mysql.connector
import MySQLdb
import os
import xlrd
import xlwt
from web_function import mysql_connect

from repo import repo_test
def mysql_connect(host,user,passwd,db,sql):
    conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    data= cursor.fetchall()
    count =1
    for row in data:
        ID= row[0]
        Username = row[1]
        password= row[2]
        # cursor.execute("update PR_GDS.MerLogin set password='1' where Username=%s and ID=%s"%(Username,ID))
        # cursor.execute("COMMIT")
        fsheet.write(count,0,Username.decode('utf8'))
        fsheet.write(count,1,password.decode('utf8'))
        print "ID=%s,Username=%s,password=%s"%(ID,Username,password)
        count+=1
    conn.close()
file = xlwt.Workbook()
bugid="bugid"
fsheet= file.add_sheet(bugid,cell_overwrite_ok=True)
fsheet.write(0,0,'Username')
fsheet.write(0,1,'Password')
sql="SELECT * FROM MerLogin ORDER BY MerchantID DESC;"
mysql_connect("prdbqa001iad.io.askjeeves.info","test","666666","PR_GDS",sql)
file.save("F:/testdata/"+bugid+".xls")

Rfile= xlrd.open_workbook("F:/testdata/"+bugid+".xls")
table = Rfile.sheet_by_name(bugid)
nrows = table.nrows
for i in range(nrows-1):
    uname=table.row(i+1)[0].value
    print uname
    repo_test(uname)