from model.group import Group

def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="99", header="group99", footer="group_footer1")
    group.id = old_groups[0].id
    app.group.update_first_group(group)
    # сначала сравним списки по длине, не загружая список групп лишний раз
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    # сравнение списков по содержанию, old - это список до обновления, поэтому добавим в его начало такой же элемент
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)