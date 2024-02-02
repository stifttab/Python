def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            # This will split the fuel and convert to integers
            x, y = map(int, fraction.split('/'))
            # This will calculate the percentage
            f = x / y
            # This will check if it is less than 1 and stop the loop
            if f <= 1:
                # This will multiply the percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    # This will return E if the percentage is less than 1
    if percentage <= 1:
        return "E"
    # This will return F if the percentage is greater than 99
    elif percentage >= 99:
        return "F"
    # This will return the %
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
