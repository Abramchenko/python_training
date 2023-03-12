# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Alexei", middlename="Petrovich", lastname="Ivanov", nickname="Alex", title=" some title",
                               company="IT one", address="Omsk", home="8(3812)463325",mobile="89139792905", work="8(3812) 465432", fax="8(3812) 465432",
                                email="anv-anv@mail.ru", email2="anv-anv@mail.ru", email3="anv-anv@mail.ru",homepage="",
                               bday="28", bmonth="May", byear="1999", aday="11", amonth="12",ayear="2019", new_group="",
                               address2="", phone2="", notes="")
    app.contact.create(contact)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)






