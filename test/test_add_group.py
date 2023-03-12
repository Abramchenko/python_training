# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="111", header="group1", footer="group_footer1")
    app.group.create(group)
    app.session.logout()
    # сначала сравним списки по длине, не загружая список групп лишний раз
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    #сравнение списков групп по содержанию
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)



'''''
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len (new_groups)
'''''




