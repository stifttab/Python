import random

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x, y = generate_integer(level)
        answer = x + y
        incorrect_attempts = 0

        while incorrect_attempts < 3:
            user_answer = input(f"{x} + {y} = ")

            try:
                user_answer = int(user_answer)

                if user_answer == answer:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
                    incorrect_attempts += 1
            except ValueError:
                print("EEE")

        if incorrect_attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {correct_answers}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in (1, 2, 3):
                raise ValueError()
            return level
        except ValueError:
            print("Invalid input. Please choose 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()
