__author__ = 'zhaor'
import mysql.connector
import MySQLdb
import os
import xlrd
import xlwt
#from web_function import mysql_connect

conn=MySQLdb.connect(host="prdbdev001iad.io.askjeeves.info",user="test",passwd="666666",db="PR_ETL_UK",charset="utf8")

def mysql_ex(sql):

    cursor = conn.cursor()
    cursor.execute(sql)
    data= cursor.fetchall()
    count =1
    for row in data:

        ProductID = row[0]
        CategoryID= row[1]
        MappingCategoryID =row[2]
        MerchantID= row[3]
       # r_CategoryID=row[4]
        # cursor.execute("update PR_GDS.MerLogin set password='1' where Username=%s and ID=%s"%(Username,ID))
        # cursor.execute("COMMIT")
        fsheet.write(count,0,ProductID)
        fsheet.write(count,1,CategoryID)
        fsheet.write(count,2,MappingCategoryID)
        fsheet.write(count,3,MerchantID)
        print "ProductID=%s,CategoryID=%s,MappingCategoryID=%s,MerchantID=%s"%(ProductID,CategoryID,MappingCategoryID,MerchantID)
        count+=1


file = xlwt.Workbook()

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]:

    bugid="Type%s"%(i)
    fsheet= file.add_sheet(bugid,cell_overwrite_ok=True)
    fsheet.write(0,0,'ProductID')
    fsheet.write(0,1,'CategoryID')
    fsheet.write(0,2,'MappingCategoryID')
    fsheet.write(0,3,'MerchantID')

    sql='''SELECT
                 MBP.ProductID,
                 PC.CategoryID,
                 MBP.MappingCategoryID,
                 MBP.MerchantID
    FROM
                 C%sMerchantBidProduct MBP,
                 C%sProduct P,
                 C%sProductCategory PC
    WHERE MBP.ProductID = P.ProductID
         AND MBP.`ProductID` = PC.`ProductID`
         AND P.type = 'FreeText'
         AND
             PC.CategoryID !=    MBP.MappingCategoryID
         AND MBP.MappingCategoryID != 0
       AND MBP.r_CategoryID != 0;'''%(i,i,i)

    print i,"----"
    mysql_ex(sql)


file.save("F:/testdata/"+str(352503)+"_GBR"+".xls")

conn.close()