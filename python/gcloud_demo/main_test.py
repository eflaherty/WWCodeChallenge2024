import pytest
import main

@pytest.fixture
def client():
    main.app.Testing = True
    return main.app.test_client()

def test_handler():
    client = main.app.test_client() # create client before each test in a fixture
    r = client.get("/")
    assert r.data.decode() == "Hello World!"
