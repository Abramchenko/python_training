# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix+"".join(
                         [random.choice(symbols) for i in range(
                                                                random.randrange(maxlen))])# случайная длина

def clear(s):
    return re.sub("  ", " ", s)

# Одна пустая и 5 непустых групп
testdata =[Contact(firstname="", lastname="", address="")]+ [Contact(
    firstname = clear(str.strip(random_string("firstname",10))), lastname = clear(str.strip(random_string("lastname",20))),
                                                         address=clear(str.strip(random_string("address",15))))
                                                   for i in  range(5)]

# 8 наборов
testdata1 = [
            Contact(firstname=firstname, lastname=lastname, address=address)
            for firstname in ["",random_string("name",10) ]
            for lastname in ["",random_string("lastname",20) ]
            for address in ["",random_string("address",15) ]
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata]) #чтобы параметр теста отображался в консоли

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

'''
contact = Contact(firstname="Alexei", middlename="Petrovich", lastname="Ivanov", nickname="Alex", title=" some title",
                               company="IT one", address="Omsk", home="8(3812)463325",mobile="89139792905", work="8(3812) 465432", fax="8(3812) 465432",
                                email="anv-anv@mail.ru", email2="anv-anv@mail.ru", email3="anv-anv@mail.ru",homepage="",
                               bday="28", bmonth="May", byear="1999", aday="11", amonth="12",ayear="2019", new_group="",
                               address2="", phone2="", notes="")
'''




