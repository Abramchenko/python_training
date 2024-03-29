import pymysql.cursors
from model.group import Group
from model.contact import Contact
#
class DBFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.database = name
        self.user = user
        self.password = password
        self.connection =pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, home=home, mobile=mobile,
                                    work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

