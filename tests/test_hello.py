from test_cicd_app import greet


def test_greet():
    assert greet("CI") == "Hello, CI!"
