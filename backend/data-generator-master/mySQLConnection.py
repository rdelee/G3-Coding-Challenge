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

con= pymysql.connect(user = 'root', passwd='123456abc!', 
                            host='localhost',
                            database = 'db_grad_cs_1917',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM deal')

        rows = cur.fetchall()

        print(rows)
        # for row in rows:
        #     print(f'{row[0]} {row[1]} {row[2]}')

finally:

    con.close()

# cur = cxn.cursor()
# rows = cur.fetchall()

# for row in rows:
#     print(row['id'], row['name'])
# cursor = cxn.cursor()
# query = ("examplequery")
# cursor.execute(query)
# for item in cursor:
#     print(item)