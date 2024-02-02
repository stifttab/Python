# Prompt the user to enter a score and convert the input to an integer
score = int(input("Score: "))

# Check the value of the score and determine the corresponding grade
if score > 89:
    # If the score is greater than 89, print "Grade: A"
    print("Grade: A")
elif score > 79:
    # If the score is greater than 79 but not greater than 89, print "Grade: B"
    print("Grade: B")
elif score > 69:
    # If the score is greater than 69 but not greater than 79, print "Grade: C"
    print("Grade: C")
else:
    # If none of the above conditions are met, print "Grade: F"
    print("Grade: F")
