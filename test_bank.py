from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

def test_return_zero():
    assert value("hello to you") == 0
    assert value("Hello") == 0
    assert value("Hello to you") == 0

def test_return_20():
    assert value("Hi") == 20
    assert value("hey") == 20

def test_return_100():
    assert value("What's up!") == 100
    assert value("good morning") == 100

if __name__ == "__main__":
    main()