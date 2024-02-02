def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        return float(d)
    except ValueError:
        print("Invalid input. Please enter a valid dollar amount.")
        return 0.0


def percent_to_float(p):
    try:
        p = p.strip('%')
        return float(p) / 100
    except ValueError:
        print("Invalid input. Please enter a valid percentage.")
        return 0.0


main()
