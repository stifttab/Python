# Define a function called convert that replaces emoticon symbols with corresponding emojis
def convert(faces):
    # Replace ":)" with a smiling emoji "🙂" and ":(" with a frowning emoji "🙁"
    return faces.replace(":)", "🙂").replace(":(", "🙁")

# Define the main function
def main():
    # Prompt the user to enter text containing emoticon symbols
    user_input = input()
    
    # Call the convert function to replace emoticons with emojis and store the result in the 'text' variable
    text = convert(user_input)
    
    # Print the converted text with emojis
    print(text)

# Call the main function to start the program
main()
