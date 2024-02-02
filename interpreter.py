# Define the main function
def main():
    # Prompt the user to enter an expression and read the input
    expression = input("Expression: ")
    
    # Split the expression into three parts: x, operator, and z
    x, operator, z = expression.split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Check the operator to determine the operation and calculate the result
    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z
    
    # Print the result with two decimal places
    print(f"{result:.2f}")

# Call the main function to start the program
if __name__ == "__main__":
    main()
