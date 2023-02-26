from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firsrtname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one"))
    app.contact.delete_first_contact()
