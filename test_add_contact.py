# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_addnew_page(wd)
        self.create_contact(wd, Contact(firsrtname="Alexei", lastname="Abramchenko", address="Omsk", company="IT one",
                                        nickname="Alex", home="8(3812)463325", mobile="89139792905",
                                        email="anv-anv@mail.ru", bday="29", bmonth="May", byear="2019"))
        self.logout(wd)
    #def test_add_empty_contact(self):
     #   wd = self.wd
      #  self.open_home_page(wd)
       # self.login(wd, username="admin", password="secret")
        #self.open_addnew_page(wd)
        #self.create_contact(wd, contactfirsrtname="", contactlastname="", contactaddress="", contactcompany="",
         #                   contactnickname="", contacthome="", contactmobile="",
          #                  contactemail="", contactbday="", contactbmonth="", contactbyear="")
        #self.logout(wd)
    def create_contact(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.contactfirsrtname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.contactlastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.contactaddress)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.contactcompany)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.contactnickname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.contacthome)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.contactmobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.contactemail)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.contactbday)
        wd.find_element_by_xpath("//option[@value='29']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.contactbmonth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.contactbyear)
        #enter_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_addnew_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")
    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
