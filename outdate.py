# Function to convert a date to YYYY-MM-DD format
def date_conversion(date_input):
    # Split the input string by spaces and commas
    parts = date_input.split()
    
    # Check if the input is in the format "month day, year"
    if len(parts) == 3 and parts[1][-1] == ',':
        month_name, day, year = parts
        if month_name in months:
            try:
                month = str(months.index(month_name) + 1).zfill(2)
                day = int(day.rstrip(','))
                year = int(year)
                if 1 <= day <= 31:
                    return f'{year:04d}-{month}-{day:02d}'
            except ValueError:
                pass

    # Try to match input in month/day/year format
    parts = date_input.split('/')
    if len(parts) == 3:
        month, day, year = parts
        try:
            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f'{year:04d}-{month:02d}-{day:02d}'
        except ValueError:
            pass

    # This will return None for the invalid input or out-of-range day
    return None

# List of month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

# This will prompt the user for input until a valid date is entered
while True:
    user_input = input("Enter a date (in month/day/year or month day, year format): ")
    date_formatted = date_conversion(user_input)
    if date_formatted:
        print(f'{date_formatted}')
        break
