import pytest
from fixture.application import Application
#perem =None
fixture = None
@pytest.fixture
#(scope="session") фикстура в процессе выполнения тестов может закрыться (внепланово), поэтому лучше создавать ее не однажды на всю сессию,
# а проверять ее валидность перед тестом, и создавать по необходимости
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid(): # если что, перезапустить фикстуру
            fixture = Application(browser=browser, base_url=base_url)
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


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/")