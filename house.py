name = input("What is your name? ")

match name:
    case "Mark" | "Desiree" | "Sadie":
        print("Family")
    case _:
        print("Not a family member")
        