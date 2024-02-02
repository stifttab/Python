def main():
    # Dictionary to store fruit names as keys and their calorie values as values
    fruit_calories = {
        "apples": 52,
        "bananas": 105,
        "oranges": 62,
        "strawberries": 32,
        "blueberries": 84,
        "grapes": 69,
        "watermelons": 30,
        "peaches": 59,
        "pears": 57,
        "cherries": 50,
        "pineapples": 83,
        "mangos": 150,
        "kiwis": 61,
        "avocados": 332,
        "grapefruits": 52,
        "lemons": 17,
        "limes": 20,
        "raspberries": 32,
        "blackberries": 40,
        "cranberries": 46,
    }

    # Prompt the user for input (fruit name)
    fruit_name = input("Enter a fruit: ").lower()

    # Check if the entered fruit is in the dictionary
    if fruit_name in fruit_calories:
        calories = fruit_calories[fruit_name]
        print(f"One portion of {fruit_name.capitalize()} has {calories} calories.")
    else:
        print("Sorry, that's not a valid fruit.")

if __name__ == "__main__":
    main()
