from random import randrange
from model.group import Group

def test_update_some_group(app,  db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="99", header="group99", footer="group_footer1")
    group.id = old_groups[index].id
    app.group.update_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    # сравнение списков по содержанию, old - это список до обновления, поэтому заменим в нем соотв. элемент
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max)==sorted(app.group.get_group_list(), key=Group.id_or_max)