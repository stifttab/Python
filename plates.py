def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #This will check if the plate start with at least two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False
    #This will check if the plate has a maximum of 6 characters
    if len(s) > 6:
        return False

    #This will check if the number came only at the end and the first number is not "0"
    if s[2:].isdigit() and s[2] == "0":
        return False
    
    #This will check if there are no numbers in the middle of the plate
    if any(char.isdigit() for char in s[:-2]):
        return False
        
    #This will check if there are no periods, spaces, or punctuation marks
    if any (char in ". ,;:!?" for char in s):
        return False
    return True

if __name__ == "__main__":
    main()