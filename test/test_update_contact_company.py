from model.contact import Contact

def test_update_contact(app):
    app.contact.update(Contact(company="BIA"))
