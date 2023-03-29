from random import randrange
from model.contact import Contact

def test_update_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                                   company="IT one"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact =Contact(firstname="IVAN",  lastname="Updated 3", nickname="Nick", title=" some new title",
                               company="IT LUX")
    id = old_contacts[index].id
    app.contact.update_contact_by_id(id, contact)
    new_contacts = db.get_contact_list()
    # сравнение списков по содержанию, в старом списке  заменим соотв. элемент
    old_contacts [index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max)==sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
