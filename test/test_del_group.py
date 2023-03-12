# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    # сначала сравним списки по длине, не загружая список групп лишний раз
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # сравнение списков по содержанию, old - это список до удаления, поэтому добавим в его начало пустой элемент
    old_groups[0:1] = []
    assert old_groups == new_groups


