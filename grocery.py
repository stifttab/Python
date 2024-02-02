# Import the defaultdict class from the collections module
from collections import defaultdict

# Define the main function
def main():
    # Create a defaultdict to store grocery items and their quantities (default to 0)
    grocery_list = defaultdict(int)

    # Prompt the user to enter items needed from the grocery store and provide instructions
    print("Enter the items you need from the grocery store (press Ctrl-D to finish):")
    
    try:
        # Start an infinite loop to receive user input
        while True:
            item = input()  # Read user input (grocery item)
            item = item.lower()  # Convert input to lowercase for case-insensitive comparison
            grocery_list[item] += 1  # Increment the quantity of the item in the grocery list
    except EOFError:
        pass  # Exit the loop when Ctrl-D (EOF) is detected

    # Sort and print the grocery list in a user-friendly format
    print("\nYour Grocery List:")
    for item, count in sorted(grocery_list.items()):
        # Capitalize the first letter of the item and display the quantity
        print(f"{count} {item.capitalize()}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
