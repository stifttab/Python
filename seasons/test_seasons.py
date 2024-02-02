from seasons import birthday_checker

def main():
    test_birthday_checker()

def test_birthday_checker():
    assert birthday_checker("1988-01-17") == ("1988", "01", "17")
    assert birthday_checker("1988-1-17") == None
    assert birthday_checker("July 3, 1988") == None
    assert birthday_checker("01-17-1988") == None

if __name__ == "__main__":
    main()

