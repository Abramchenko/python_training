# -*- coding: utf-8 -*-
#import pytest
from model.group import Group
from data.groups import testdata

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata]) #чтобы параметр теста отображался в консоли

def test_add_group(app, json_groups):
    group = json_groups
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






