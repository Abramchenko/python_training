import pytest
from fixture.application import Application

fixture = None
@pytest.fixture
#(scope="session") фикстура в процессе выполнения тестов может закрыться (внепланово), поэтому лучше создавать ее не однажды на всю сессию,
# а проверять ее валидность перед тестом, и создавать по необходимости
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid(): # если что, перезапустить фикстуру
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")   # гарантированный логин
    return fixture

# такая фикстура выполняется один раз, в конце
@pytest.fixture(scope="session", autouse=True) # нигде не используется
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
