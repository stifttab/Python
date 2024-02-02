# Import the random module to generate random integers
import random

# Define the main function
def main():
    # Prompt the user for a level (positive integer)
    while True:
        try:
            level = int(input("Enter a Level: "))  # Read user input as an integer
            if level <= 0:
                raise ValueError("Please enter a positive integer.")  # Raise an error for non-positive input
            break  # Exit the loop if a valid input is provided
        except ValueError:
            print("Your input is Invalid. Please enter a positive integer only!")

    # Generate a random integer between 1 and the specified level (inclusive)
    target = random.randint(1, level)

    while True:
        # Prompt the user to guess the integer (positive integer)
        while True:
            try:
                guess = int(input(f"Guess the integer between 1 and {level}: "))  # Read user's guess
                if guess <= 0:
                    raise ValueError("Enter a positive integer.")  # Raise an error for non-positive input
                break  # Exit the loop if a valid input is provided
            except ValueError:
                print("Your input is Invalid. Please enter a positive integer only")  # Handle invalid input

        # Compare the guess with the target integer
        if guess < target:
            print("Too small!")  # Provide feedback if the guess is smaller
        elif guess > target:
            print("Too large!")  # Provide feedback if the guess is larger
        else:
            print("Just right!")  # Provide feedback if the guess is correct
            break  # Exit the loop when the guess is correct

if __name__ == "__main__":
    main()  # Call the main function to start the game
