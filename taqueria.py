from collections import defaultdict

def main():
    grocery_list = defaultdict(int)

    print("Enter the items you need from the grocery store (press Enter on an empty line to finish):")
    while True:
        item = input()
        if not item:  # Check for an empty line to end input
            break
        item = item.lower()  # Convert input to lowercase for case-insensitive comparison
        grocery_list[item] += 1

    # Sort and print the grocery list with capitalized item names
    print("\nYour Grocery List:")
    for item, count in sorted(grocery_list.items()):
        capitalized_item = item.capitalize()  # Capitalize the item name
        print(f"{count} {capitalized_item}")

if __name__ == "__main__":
    main()
