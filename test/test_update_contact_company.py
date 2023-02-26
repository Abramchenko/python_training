from model.contact import Contact

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firsrtname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one"))
    app.contact.update(Contact(company="NEW"))
