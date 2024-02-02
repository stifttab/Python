# Import the 'inflect' library to handle pluralization and formatting of names
import inflect

# Function to format the farewell message based on the number of names
def bid_adieu(names):
    # Create an instance of the inflect engine
    p = inflect.engine()
    
    if len(names) == 1:
        # If there's only one name, format the message accordingly
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        # If there are two names, format the message accordingly
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        # If there are more than two names, format the message with commas and "and"
        formatted_names = ", ".join(names[:-1])
        return f"Adieu, adieu, to {formatted_names}, and {names[-1]}"

# Main function where user input is collected
def main():
    names = []  # Initialize an empty list to store names
    print("Enter names one per line (press Ctrl-D to finish):")
    
    try:
        while True:
            name = input()  # Read names from the user
            names.append(name)  # Add each name to the list
    except EOFError:
        pass  # Ctrl-D was pressed to exit the input loop
    
    if names:
        # Call the bid_adieu function to format the farewell message
        farewell = bid_adieu(names)
        print(farewell)  # Print the farewell message

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function when the script is executed
