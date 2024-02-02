# Define the main function
def main():
    # Start an infinite loop to repeatedly prompt the user for input until valid input is provided
    while True:
        try:
            # Prompt the user to enter a fraction
            fraction = input("Please enter a fraction: ")
            
            # Split the fraction input into two integers, x and y
            x, y = map(int, fraction.split('/'))
            
            # Check for invalid inputs
            if y <= 0 or x > y:
                raise ValueError("Invalid input. Both X and Y should be positive integers.")
            
            # Check if x is equal to 0 (meaning it's effectively 0%)
            if x == 0:
                print("E")
            else:
                # Calculate the percentage and round it to the nearest integer
                percentage = (x / y) * 100

                # Determine the grade based on the percentage
                if percentage <= 1:
                    print("E")
                elif percentage >= 99:
                    print("F")
                else:
                    # Print the percentage with no decimal places
                    print("{:.0f}%".format(round(percentage)))
            
            # Exit the loop if valid input was processed
            break
        except (ValueError, ZeroDivisionError):
            # Handle exceptions for invalid input and provide an error message
            print("Your input is invalid! Please try again.")

# Call the main function to start the program
main()
