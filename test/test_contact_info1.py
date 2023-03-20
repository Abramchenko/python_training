import re
from random import randrange
from model.contact import Contact


def test_contact_info_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title", company="IT one",
                            home="463325", mobile="89139790510", work="8949", email="a1@mail.ru", email2="a2@mail.ru", email3="a3@mail.ru",
                                   address="RF, City, Street A, number 13"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)

    #assert contact_from_home_page.home == clear (contact_from_edit_page.home)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(
        filter(lambda x: x!="",      # избавиться от пустых строк (в конце добавился \n)
        map(lambda x: clear(x),                   # применить clear ко всем телефонам по отдельности
        filter(lambda x: x is not None, [contact.home, contact.mobile,contact.work])))) # отобрать только не None телефоны


def merge_emails_like_on_homepage(contact):
    return "\n".join(
        filter(lambda x: x!="",      # избавиться от пустых строк (в конце добавился \n)
        map(lambda x: clear(x),                   # применить clear ко всем телефонам по отдельности
        filter(lambda x: x is not None, [contact.email, contact.email2,contact.email3])))) # отобрать только не None телефоны

'''
def test_phone_on_contactview_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    assert contact_from_home_page.home == clear(contact_from_view_page.home)
    assert contact_from_home_page.work == clear(contact_from_view_page.work)
    assert contact_from_home_page.mobile == clear(contact_from_view_page.mobile)
'''





