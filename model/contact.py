from sys import maxsize
import re


def clear_spaces(s):
    return re.sub(" {2}", " ", s)
class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None,company=None, address=None,
                 home=None,mobile=None, work=None, all_phones=None, all_emails = None,
                 fax=None,email=None, email2=None, email3=None,homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None,ayear=None, new_group=None, address2=None, phone2=None, notes=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.homepage = homepage
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address, self.all_emails, self.all_phones)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (clear_spaces(self.lastname.strip()) == clear_spaces(other.lastname.strip()) and clear_spaces(self.firstname.strip()) == clear_spaces(other.firstname.strip()))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
