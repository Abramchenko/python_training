# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_add_contact(app, db, orm, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = orm.get_contact_list()

    groups = orm.get_group_list()
    group = random.choice(groups)
    names = [group.name, "[none]"]
    name = random.choice(names)
    contact.new_group = name

    app.contact.create(contact)
    new_contacts = orm.get_contact_list()

    # сравнение списков по содержанию, добавим такой же элемент в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.contact.get_contact_list(), key=Contact.id_or_max)






