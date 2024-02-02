import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        name = input("Type your name: ")
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("")
