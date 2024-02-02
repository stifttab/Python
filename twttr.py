def main():
    user_input = input("Enter a text: ")
    result = shorten(user_input)
    print("Text without vowels:", result)

def shorten(word):
    vowels = "AEIOUaeiou"
    text_without_vowels = ""

    for char in word:
        if char not in vowels:
            text_without_vowels += char
    
    return text_without_vowels 

if __name__ == "__main__":
    main() 