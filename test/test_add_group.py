# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix+"".join(
                         [random.choice(symbols) for i in range(
                                                                random.randrange(maxlen))])# случайная длина
def clear(s):
    return re.sub("  ", " ", s)

# Одна пустая и 5 непустых групп
testdata =[Group(name="", header="", footer="")]+ [Group( name = clear(str.strip(random_string("name",10))),
                                                          header = clear(str.strip(random_string("header",20))),
                                                         footer=clear(str.strip(random_string("footer",15))))
                                                   for i in  range(5)]

# 8 наборов
testdata1 = [
            Group(name=name, header=header, footer=footer)
            for name in ["",random_string("name",10) ]
            for header in ["",random_string("header",20) ]
            for footer in ["",random_string("footer",15) ]
]
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata]) #чтобы параметр теста отображался в консоли

def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    #group = Group(name="111", header="group1", footer="group_footer1")
    app.group.create(group)
    app.session.logout()
    # сначала сравним списки по длине, не загружая список групп лишний раз
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    # сравнение списков групп по содержанию
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)






