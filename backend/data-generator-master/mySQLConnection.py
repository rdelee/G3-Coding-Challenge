import mysql.connector
from mysql.connector import errorcode
#import requests

try:
    cnx = mysql.connector.connect(host='mysql-server' ,user='root',password='', database = "db_grad_cs_1917")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

mycursor = cnx.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)