from model.contact import Contact

# Внутренний тест, что загрузка из БД одинаковая с web
# В БД инфо более точная, с пробелами в name, их приходится очищать
def test_contact_list(app, db):    #две фикстуры
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, lastname = contact.lastname.strip(), firstname = contact.firstname.strip())
    db_list = map(clean,db.get_contact_list())
    assert sorted(ui_list, key = Contact.id_or_max) == sorted(db_list, key = Contact.id_or_max)

    assert False