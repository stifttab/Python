def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f"${result}")

def value(greeting):
    #This will convert the greeting in all lower and without whitespaces
    greeting = greeting.lower().strip()
    #This will check if the aswer has the word "hello", then will return 0
    if "hello" in greeting:
        return 0
    #This will check if the answer start with "h", return 20
    elif "h" == greeting[0]:
        return 20
    #This will return 100
    else:
        return 100

if __name__ == "__main__":
    main()
