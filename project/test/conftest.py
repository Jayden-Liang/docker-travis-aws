import pytest

from project.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once( scope ='session').
    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }
    _app = create_app(settings_override=params)
    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()

@pytest.yield_fixture(scope='function') #好像跟跟踪cookie等有关
def client(app):
    """
    Setup an app client, this gets executed for each test function.
    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
