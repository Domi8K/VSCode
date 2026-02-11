"""
names = []

for _ in range(3):
    # name = input("What is your name? ")
    names.append(input("What's you name? "))

for name in sorted(names):
    print(f'hello, {name}')
"""

# saving to a file

name = input("What's your name? ")

"""
file = open("names.txt", "a+") # 'a' for append, 'w' for write
file.write(f'{name}\n')
file.close()
"""

# this automatically closes the file but works the same as the former

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')