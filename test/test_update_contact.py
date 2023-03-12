from model.contact import Contact

def test_update_contact(app):

    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                                   company="IT one"))
    old_contacts = app.contact.get_contact_list()
    contact =Contact(firstname="IVAN",  lastname="Updated 2", nickname="Nick", title=" some new title",
                               company="IT LUX")
    contact.id = old_contacts[0].id
    app.contact.update(contact)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, в старый список добавим такой же элемент в начало
    old_contacts [0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)