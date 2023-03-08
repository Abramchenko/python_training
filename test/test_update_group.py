from model.group import Group

def test_update_first_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="99", header="group99", footer="group_footer1")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)