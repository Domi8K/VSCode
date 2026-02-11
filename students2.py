import csv

name = input('What is your name? ')
home = input('Where is your house? ')

with open('students2.csv', 'a') as file:
    """
    writer = csv.writer(file)
    writer.writerow([name, home])"""
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name, 'home': home})