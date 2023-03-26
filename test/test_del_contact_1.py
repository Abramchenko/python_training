import random
from random import randrange

from model.contact import Contact

def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    # сравнение списков по содержанию, в старом списке удалим выбранный элемент
    old_contacts.remove(contact)
    assert old_contacts == new_contacts