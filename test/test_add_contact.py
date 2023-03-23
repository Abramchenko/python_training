# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, djson_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)






