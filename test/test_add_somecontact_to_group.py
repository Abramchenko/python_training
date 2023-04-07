from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db, orm, json_contacts, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(not_in_group)
    app.contact.add_contact_to_group(contact.id, group.name)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts_in_group, key = Contact.id_or_max)
    #if check_ui:
    #    assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.contact.get_contact_list(), key=Contact.id_or_max)