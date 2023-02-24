# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.create(Contact(firsrtname="Alexei", lastname="Abramchenko", address="Omsk", company="IT one",nickname="Alex", home="8(3812)463325",
                               mobile="89139792905", email="anv-anv@mail.ru", bday="28", bmonth="May", byear="2019"))
    app.session.logout()






