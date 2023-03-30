from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    #l = db.get_contact_list()
    l = db.get_contacts_in_group(Group(id="75"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #ORM сам закрывается



'''
from fixture.db import DBFixture
db = DBFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()
'''
'''
import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
try:
    cursor=connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():               # fetchall() необязательный
        print(row)
finally:
    connection.close()
'''

