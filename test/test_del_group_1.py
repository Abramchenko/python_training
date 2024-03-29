import random

from model.group import Group

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    # сравнение списков по содержанию, old - это список до удаления, поэтому удалим в нем выбранный элемент
    old_groups.remove(group)
    assert old_groups == new_groups