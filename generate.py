# Import the sys module to access command-line arguments
import sys 

try:
    # Try to access the command-line argument at index 1 (the first argument after the script name)
    # and print a greeting message with the provided name
    print("hello, my name is", sys.argv[1])
except IndexError:
    # Handle the IndexError exception if no command-line argument is provided
    # and print a message prompting the user to say their name
    print("Say your name!")
