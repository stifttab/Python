import sys  # Import the sys module to access command-line arguments and exit the program.
from pyfiglet import Figlet  # Import the Figlet class from the pyfiglet module.

def get_random_font():
    return Figlet().getFonts()[0]  # Get the first font from the available fonts list.

def command_line():
    if len(sys.argv) == 1:  # Check if no command-line arguments were provided.
        return get_random_font()  # Return a random font if no arguments were given.
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):  # Check for valid arguments.
        return sys.argv[2]  # Return the font name provided as an argument.
    else:
        return None  # Return None if the arguments are not valid.

def main():
    font_name = command_line()  # Get the font name from the command-line arguments.

    if font_name is None:
        sys.exit("Invalid usage")  # Exit with an error message if the arguments are invalid.

    if font_name not in Figlet().getFonts():  # Check if the specified font is available.
        sys.exit(f"Invalid usage")  # Exit with an error message if the font is not found.

    user_text = input("Enter text: ")  # Prompt the user to enter text.

    try:
        figlet = Figlet(font=font_name)  # Create a Figlet object with the specified font.
        output_text = figlet.renderText(user_text)  # Render the user's text in the chosen font.
        print(output_text)  # Print the rendered text.
    except Exception as e:
        sys.exit(f"Error: {e}")  # Exit with an error message if there's an exception.

if __name__ == "__main__":
    main()  # Execute the main function when the script is run.
