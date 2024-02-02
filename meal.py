def main():
    time = input("What time is it?: ")
    hours = convert(time)
    
    if 7.0 <= hours < 8.0:
        print("It's breakfast time!")
    elif 12.0 <= hours < 13.0:
        print("It's lunch time!")
    elif 18.0 <= hours < 19.0:
        print("It's dinner time!")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
