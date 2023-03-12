from random import randrange

from model.contact import Contact

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrovich", nickname="Alex", title=" some title",
                               company="IT one"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    # сначала сравним списки по длине, не загружая список лишний раз
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # сравнение списков по содержанию, в старый список добавим пустой элемент № index
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts