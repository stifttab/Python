from twttr import shorten

def main():
    test_word()

def test_word():
    assert shorten("Hello") == "Hll"
    assert shorten("Python") == "Pythn"
    assert shorten("") == ""
    assert shorten("AEIOUaeiou") == ""
    assert shorten("aeiouAEIOU") == ""
    assert shorten("AEIOU") == ""
    assert shorten("AaEeIiOoUu") == ""
    assert shorten("Banana") == "Bnn"
    assert shorten("1234567890") == "1234567890"
    assert shorten("Hello123") == "Hll123"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
    assert shorten("Hello, World!") == "Hll, Wrld!"

if __name__ == "__main__":
    main()