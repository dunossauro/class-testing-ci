from src.functions import add


def test_01():
    assert add.__annotations__ == {'x': int, 'y': int}
