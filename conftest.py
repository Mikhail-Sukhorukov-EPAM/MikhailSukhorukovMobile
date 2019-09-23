import pytest
from Application.AppiumApp import App

@pytest.fixture(scope="session")
def appfixture():
    app = App()
    yield app
    app.destroy()