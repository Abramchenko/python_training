# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    #group = Group(name="111", header="group1", footer="group_footer1")
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    # сравнение списков групп по содержанию
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)