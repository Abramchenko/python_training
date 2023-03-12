# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    # сначала сравним списки по длине, не загружая список групп лишний раз
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # сравнение списков по содержанию, old - это список до удаления, поэтому добавим на место удаленного пустой элемент
    old_groups[index:index+1] = []
    assert old_groups == new_groups


