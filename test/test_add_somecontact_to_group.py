from model.contact import Contact
import random
from model.group import Group

def test_add_contact_to_group(app, orm):
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
        groups = orm.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(group)

    contact = Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one")
    if (len(orm.get_contact_list())==0) or (len(orm.get_contacts_not_in_group)) == 0:
        app.contact.create(contact)
    not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(not_in_group)
    app.contact.add_contact_to_group(contact, group)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    # сравнение списков по содержанию, добавим такой же элемент в старый список
    assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts_in_group, key = Contact.id_or_max)
