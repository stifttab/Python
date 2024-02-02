import sys
import csv
from tabulate import tabulate
def main():
    count_the_line_of_codes()

    #Create variable to store the table data
    menu = []
    
    #Try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)
    #If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    #Print the menu
    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))

def count_the_line_of_codes():
    #Check how many elements in the command line
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    #Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
if __name__ == "__main__":
    main()
