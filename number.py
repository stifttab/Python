def main():
    x = get_int("what is x? ")
    print(f"x is {x}")

def get_int(answer):
    while True:
        try:
            return int(input(answer))        
        except ValueError:
            print("This is not a integer!")
                 
    
main()