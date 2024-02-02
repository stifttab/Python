def main():
    # Initialize variables
    amount_need = 50  # Initial price in cents
    total_inserted = 0

    # Prompt the user to insert coins until enough money is inserted
    while total_inserted < amount_need:
        coin = int(input("Insert a coin (25/10/5 cents): "))
        if coin in [25, 10, 5]:
            total_inserted += coin
            print(f"Amount due: {amount_need - total_inserted} cents remaining.")
        else:
            print("Invalid coin. Accepted denominations: 25, 10, 5 cents.")

    # Calculate and display change
    change = total_inserted - amount_need
    if change > 0:
        print(f"Thank you! Your change is {change} cents.")
    else:
        print("Thank you!")

if __name__ == "__main__":
    main()
