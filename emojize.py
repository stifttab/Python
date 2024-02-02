import emoji

def emojize_text(input_text):
    # This use the emoji library to emojize the input text
    emojized_text = emoji.emojize(input_text)
    return emojized_text

def main():
    # Prompt the user for input
    user_input = input("Input here: ")

    # Emojize the user input
    emojized_result = emojize_text(user_input)

    # Print the emojized text
    print("Output:", emojized_result)


if __name__ == "__main__":
    main()
