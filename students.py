import csv

name = input("What is your name? ")
home = input("Where do you live? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
    