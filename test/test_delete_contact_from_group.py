import random
from model.group import Group
from model.contact import Contact
def test_del_contact_from_group(app, db, orm, check_ui):
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
        groups = orm.get_group_list()
    group = random.choice(groups)

    old_contacts_in_group = orm.get_contacts_in_group(group)

    if len(old_contacts_in_group) == 0:
        contacts = orm.get_contact_list()
        if len(contacts) == 0:
            app.contact.create(Contact(firstname="first2", lastname="last2", address="addr2", mobile="222-22"))

        not_in_group = orm.get_contacts_not_in_group(group)
        if len(not_in_group) == 0:
            app.contact.create(Contact(firstname="first1", lastname="last1", address="addr1", mobile="111-11"))
            not_in_group = orm.get_contacts_not_in_group(group)

        contact = random.choice(not_in_group)
        app.contact.add_contact_to_group(contact, group)

    old_contacts_in_group = orm.get_contacts_in_group(group)

    contact = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(contact, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)

    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(old_contacts_in_group, key=Contact.id_or_max)