# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinilizer(fixture.destroy)
    return fixture
def test_add_contact(app):

    app.login( username="admin", password="secret")
    app.create_contact( Contact(firsrtname="Alexei", lastname="Abramchenko", address="Omsk", company="IT one",
                                nickname="Alex", home="8(3812)463325", mobile="89139792905",
                                email="anv-anv@mail.ru", bday="28", bmonth="May", byear="2019"))
    app.logout()






