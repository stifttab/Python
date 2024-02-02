from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = birthday_checker(birthday)
    except:
        sys.exit("Invalid Date")
    date_of_birthday = date(int(year), int(month), int(day))
    todays_date = date.today()
    age_today = todays_date - date_of_birthday
    total_minutes = age_today.days * 24 * 60
    final_output = p.number_to_words(total_minutes, andword="")

    print(final_output.capitalize() + " minutes")

def birthday_checker(birthday):
    if re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
