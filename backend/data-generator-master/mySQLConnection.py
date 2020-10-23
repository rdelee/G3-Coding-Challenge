# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='db_grad_cs_1917',
#                                          user='root',
#                                          password='')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

import pymysql

connection= pymysql.connect(user = 'root', passwd='123456abc!', 
                            host='mysql-server',
                            database = 'db_grad_cs_1917')

cursor = connection.cursor()
query = ("MYQUERY")
cursor.execute(query)
for item in cursor:
    print(item)