import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    timeFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if timeFormat:
        value = timeFormat.groups()
        if int(value[1]) > 12 or int(value[5]) > 12:
            raise ValueError
        first_format = time_output(value[1], value[2], value[3])
        second_format = time_output(value[5], value[6], value[7])
        return f"{first_format} to {second_format}"
    else:
        raise ValueError

def time_output(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            time_hour = 12
        else:
            time_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            time_hour = 0
        else:
            time_hour = int(hour)
    if minute == None:
        time_minute = ":00"
        new_time_format = f"{time_hour:02}" + time_minute
    else:
        new_time_format = f"{time_hour:02}" + ":" + minute
    return new_time_format


if __name__ == "__main__":
    main()
