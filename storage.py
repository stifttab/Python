from bank import value
def main():
    #This will call test functions
    test_return_zero()
    test_return_20()
    test_return_100()

#This will return 0 for this Test
def test_return_zero():
    assert value("hello to you") == 0
    assert value("Hello") == 0
    assert value("Hello to you") == 0

#This will return 20 for this Test
def test_return_20():
    assert value("Hi") == 20
    assert value("hey") == 20

#This will retrun 100 for this Test

def test_return_100():
    assert value("What's up!") == 100
    assert value("good morning") == 100
if __name__ == "__main__":
    main()