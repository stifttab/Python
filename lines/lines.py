import sys  # Import the sys module to work with command-line arguments.

def is_comment_or_blank(line):
    # This function checks if a given line is a comment or blank (whitespace).
    # It returns True if it's a comment (starts with '#') or if it's blank (only whitespace), otherwise False.
    return line.strip().startswith("#") or not line.strip()

def count_lines_of_code(filename):
    try:
        # Attempt to open the specified file in read ('r') mode.
        with open(filename, "r") as file:
            lines = file.readlines()  # Read all lines of the file into a list.
            line_count = sum(1 for line in lines if not is_comment_or_blank(line))
            # Count the lines that are not comments or blank lines using a generator expression and sum.
            return line_count

    except FileNotFoundError:
        sys.exit("File does not exist")  # Handle the case where the specified file does not exist.

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")  # Check if there are too few command-line arguments.

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")  # Check if there are too many command-line arguments.

    filename = sys.argv[1]  # Get the filename from the command-line arguments.
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")  # Check if the file does not have a .py extension.

    line_count = count_lines_of_code(filename)  # Count the lines of code in the specified file.
    print(line_count)  # Print the line count.
