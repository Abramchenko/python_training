import random

def test_del_contact_from_group(app, db, orm, check_ui):
    groups = orm.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    if len(old_contacts_in_group) == 0:
        not_in_group = orm.get_contacts_not_in_group(group)
        contact = random.choice(not_in_group)
        app.contact.add_contact_to_group(contact.id, group.name)
        old_contacts_in_group = orm.get_contacts_in_group(group)

    contact = random.choice(old_contacts_in_group)

    #print('\n', contact.id, group.id, group.name)
    app.contact.remove_contact_from_group(contact.id, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert old_contacts_in_group == new_contacts_in_group