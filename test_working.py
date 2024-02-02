from working import convert
import pytest

def main():
    test_wrong_time_hour_minute()
    test_time_output()
    test_wrong_format()

def test_wrong_time_hour_minute():
    with pytest.raises(ValueError):
        convert("15 PM to 23 PM")
        convert("11:60 AM to 11:60 PM")

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_time_output():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

if __name__ == "__main__":
    main()
