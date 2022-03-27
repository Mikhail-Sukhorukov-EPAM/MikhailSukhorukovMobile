import pytest
from applications.appium_app import App


@pytest.fixture(scope="session")
def app():
    app = App()
    yield app
    app.destroy()
