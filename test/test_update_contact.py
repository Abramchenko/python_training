from random import randrange

from model.contact import Contact

def test_update_contact(app):

    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                                   company="IT one"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact =Contact(firstname="IVAN",  lastname="Updated 3", nickname="Nick", title=" some new title",
                               company="IT LUX")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(index, contact)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, в старом списке  заменим соотв. элемент
    old_contacts [index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)