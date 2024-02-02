import emoji

def emoji_text(emoji_text):
    
    emoji_text = emoji.emojize(emoji_text)
    return emoji_text

def main():

    user_input = input("Input here: ")
    emoji_result = emojize_text(user_input)
    print("Output:", emoji_result)

if __name__ == "__main__":
    main()
