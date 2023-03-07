from model.contact import Contact

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                                   company="IT one"))
    old_contacts = app.contact.get_contact_list()
    app.contact.update(Contact(firstname="IVAN ",  lastname="Updated 2", nickname="Nick", title=" some new title",
                               company="IT LUX"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
