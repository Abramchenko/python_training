import pymysql.cursors
#
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor=connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():               # fetchall() необязательный
        print(row)
finally:
    connection.close()

