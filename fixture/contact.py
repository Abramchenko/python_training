from random import randrange
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from model.contact import Contact


class ContactHelper():
    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_addnew_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_contact_to_group(self, id, group_name):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_name("to_group").send_keys(group_name)
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def remove_contact_from_group(self, id, group):
        wd = self.app.wd
        self.open_contacts_page()
        #print(id, group.id, group.name)
        text = group.name
        #wd.find_element_by_name("group").click()
        #wd.find_element_by_name("group").send_keys("[none]")
        wd.find_element_by_name("group").click()
        wd.find_element_by_name("group").send_keys(text)
        self.select_contact_by_id(id)
        #wd.find_element_by_css_selector("input[name='remove']").click()
        wd.find_element_by_name("remove").click()
        self.contact_cache = None
        #wd.find_element_by_css_selector("a[href='./?group=%s']" % group_name).click()

    def create(self, contact):
        wd = self.app.wd
        self.open_addnew_page()
        self.fill_contact_form(contact)
        # enter_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("new_group", contact.new_group)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            if not(field_name in ("bday","bmonth", "aday", "amonth", "new_group")):
                wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self, index):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.open_contacts_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.open_contacts_page()
        self.contact_cache = None
    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or (wd.current_url.endswith("/index.php"))):
            wd.find_element_by_link_text("home").click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" %id).click()

    def update_first_contact(self, new_contact_data):
        self.update_contact_by_index(0, new_contact_data)

    def update_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # select contact to edit
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def update_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        # select contact to edit
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" %str(id)).click()


    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        # собираем список в том случае, если в кэше его нет
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache  = []
            for row in wd.find_elements_by_name("entry"):
                id = row.find_element_by_name("selected[]").get_attribute("value")
                cells = row.find_elements_by_tag_name("td")
                lastname_text = row.find_element_by_xpath("td[2]").text
                if lastname_text is None:
                    lastname_text =""
                firstname_text = row.find_element_by_xpath("td[3]").text
                if firstname_text is None:
                    firstname_text =""
                address = cells[3].text
                # или id = row.find_element_by_tag_name("input").get_attribute("value")
                # телефоны по отдельности
                #all_phones = cells[5].text.splitlines()
                #self.contact_cache.append(Contact(id=id, firstname=firstname_text, lastname=lastname_text,
                 #                         home=all_phones[0], mobile=all_phones[1], work= all_phones[2] ))
                                            #fax =all_phones[3]
                # email, телефоны вместе
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname_text, lastname=lastname_text, address=address,
                                         all_phones=all_phones, all_emails=all_emails))
        return list(self.contact_cache)   #это копия списка


    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname_text = wd.find_element_by_name("lastname").get_attribute("value")
        firstname_text = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        email =wd.find_element_by_name("email").get_attribute("value")
        email2 =wd.find_element_by_name("email2").get_attribute("value")
        email3 =wd.find_element_by_name("email3").get_attribute("value")
        #fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(id=id, firstname=firstname_text, lastname=lastname_text, address = address,
                        home=home, mobile=mobile, work= work, email=email, email2=email2, email3=email3)



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[7]/a/img").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        # телефоны собраны в одом объекте с новой строки
        text = wd.find_element_by_id ("content").text
        # ищем строку после символов Н:
        home = re.search("H:(.*)", text).group(1)
        mobile = re.search("M:(.*)", text).group(1)
        work = re.search("W:(.*)", text).group(1)
        lastname_text = wd.find_element(By.XPATH, "/html/body/div/div[4]/b").get_attribute("value")
        # fax = re.search("F:(.*)", text).group(1)
        return (Contact(lastname=lastname_text,home=home, mobile=mobile, work=work))



