import sys  # Import the sys module, which provides access to command-line arguments and system-specific functionality.
import csv  # Import the csv module, which allows reading and writing CSV files.

def main():
    checking_arg()  # Call the checking_arg function to validate command-line arguments.
    results = []  # Initialize an empty list to store the cleaned data.

    try:
        with open(sys.argv[1], "r") as csvfile:  # Open the input CSV file for reading.
            reader = csv.DictReader(csvfile)  # Create a CSV reader to read the input file as a dictionary.
            for row in reader:  # Iterate through each row in the input CSV file.
                remove_name_comma = row["name"].split(",")  # Split the "name" field by a comma.
                results.append({'first': remove_name_comma[1].lstrip(), "last": remove_name_comma[0], "house": row["house"]})  # Append a dictionary to the results list with cleaned data.

        with open(sys.argv[2], "w") as newfile:  # Open the output CSV file for writing.
            writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])  # Create a CSV writer for the output file.
            writer.writeheader()  # Write the header row to the output CSV file.
            for row in results:  # Iterate through the cleaned data.
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})  # Write each row of data to the output CSV file.

    except FileNotFoundError:  # Handle the case where the input file is not found.
        sys.exit(f"Could not read {sys.argv[1]}")  # Exit with an error message.

def checking_arg():
    if len(sys.argv) > 3:  # Check if there are too many command-line arguments.
        sys.exit("Too many command-line arguments")  # Exit with an error message.
    if len(sys.argv) < 3:  # Check if there are too few command-line arguments.
        sys.exit("Too few command-line arguments")  # Exit with an error message.
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:  # Check if the provided file names end with ".csv."
        sys.exit("These are not CSV files")  # Exit with an error message.

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly.
