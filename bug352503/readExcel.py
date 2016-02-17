__author__ = 'zhaor'
import MySQLdb
import os
import xlrd
import xlwt
#from web_function import mysql_connect
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file= 'file.xls',by_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(by_index)
    nrows = table.nrows
    ncols = table.ncols
    list =[]
    for rownum in range(1,nrows):
        ilist=[]
        row = table.row_values(rownum)
        for i in range(ncols):
                ilist.append(int(row[i]))

        list.append(ilist)
    return list

x="F:\\testdata\\"+str(352503)+"_SE"+".xlsx"
#x="F:\q.xls"
print x
print excel_table_byindex(x,1)
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="price",charset="utf8")
name= "SE_"+str(352503)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS %s" % name)



sql="""CREATE TABLE %s (
         ProductID  CHAR(20) NOT NULL primary key,
         CategoryID  CHAR(20),
         MappingCategoryID CHAR(20),
         MerchantID  CHAR(20)
         )"""%name
cursor.execute(sql)

sql = "insert into "+name+" (ProductID,CategoryID,MappingCategoryID,MerchantID) values (%s, %s,%s,%s)"


#param =[['570709984','483','187','483'],['1','496','72','11']]
for i in range(0,19):
    param=excel_table_byindex(x,i)

    try:
        cursor.executemany(sql, param)
        conn.commit()
        print "success insert many records!"+str(i)
    except Exception, e:
        conn.rollback()
        print e


conn.close()