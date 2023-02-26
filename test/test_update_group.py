from model.group import Group

def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(name="99", header="group99", footer="group_footer1"))
