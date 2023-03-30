import re
from model.contact import Contact

def clear(s):
    return re.sub("[() -]", "", s)


def clear_spaces(s):
    return re.sub(" {2}", " ", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(
        filter(lambda x: x!="",      # избавиться от пустых строк (в конце добавился \n)
        map(lambda x: clear(x),                   # применить clear ко всем телефонам по отдельности
        filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))) )# отобрать только не None телефоны

def merge_emails_like_on_homepage(contact):
    return "\n".join(
        filter(lambda x: x!="",      # избавиться от пустых строк (в конце добавился \n)
        filter(lambda x: x is not None, [contact.email, contact.email2,contact.email3]))) # отобрать только не None email


def test_contacts_homepage_db(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title", company="IT one",
                            home="463325", mobile="89139790510", work="8949", email="a1@mail.ru", email2="a2@mail.ru", email3="a3@mail.ru",
                                   address="RF, City, Street A, number 13"))
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(0, app.contact.count()):
        assert ui_contacts[i].id == db_contacts[i].id
        assert ui_contacts[i].firstname == clear_spaces(db_contacts[i].firstname)
        assert ui_contacts[i].lastname == clear_spaces(db_contacts[i].lastname)
        assert ui_contacts[i].address == clear_spaces(db_contacts[i].address)
        print(db_contacts[i])
        assert ui_contacts[i].all_phones == merge_phones_like_on_homepage(db_contacts[i])
        #assert ui_contacts[i].email == db_contacts[i].email
        assert ui_contacts[i].all_emails == merge_emails_like_on_homepage(db_contacts[i])
        #assert ui_contacts[i].all_phones == merge_phones_like_on_homepage(db_contacts[i])