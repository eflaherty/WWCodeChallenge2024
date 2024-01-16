import pytest
import main

@pytest.fixture
def client():
    main.app.Testing = True
    return main.app.test_client()

def test_handler():
     r = client.get("/")
     assert r.data.decode() == "Hello World!"
