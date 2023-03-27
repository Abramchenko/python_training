# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.group.get_group_list(), key=Contact.id_or_max)






