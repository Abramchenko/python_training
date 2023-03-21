from fixture.application import Application
import pytest
import json
import os.path


fixture = None
target = None
@pytest.fixture
#(scope="session") фикстура в процессе выполнения тестов может закрыться (внепланово), поэтому лучше создавать ее не однажды на всю сессию,
# а проверять ее валидность перед тестом, и создавать по необходимости
def app(request):
    global fixture # говорим, что будем их использовать
    global target
    browser = request.config.getoption("--browser")
    if target is None:   # чтобы открыть его и считать однажды вначале
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)

    if fixture is None or not fixture.is_valid(): # если что, перезапустить фикстуру
        fixture = Application(browser=browser, base_url= target["base_url"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])   # гарантированный логин
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
    parser.addoption("--target", action="store", default="target.json")
#"http://localhost/addressbook/")