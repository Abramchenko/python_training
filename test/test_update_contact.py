from model.contact import Contact

def test_update_contact(app):
    app.contact.update(Contact(firsrtname="Alexei", middlename="Petrovich", lastname="Updated 2", nickname="Alex", title=" some title",
                               company="IT one", address="Omsk", home="8(3812)463325",mobile="89139792905", work="8(3812) 465432",
                                fax="8(3812) 465432", email="anv-anv@mail.ru", email2="anv-anv@mail.ru", email3="anv-anv@mail.ru",homepage="",
                               bday="28", bmonth="May", byear="1999", aday="11", amonth="12",ayear="2019", new_group="",
                               address2="", phone2="", notes=""))
