
# using a while loop to meow 3 times
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

# using a for loop to meow 3 times but the problem with this is that you have to list down the numbers
# and it is not dynamic
"""
for i in [0, 1, 2]:
    print("meow")
"""
# a better way to do this is to use the range function
"""

for i in range(3):
    print("meow") 
"""
    
# if you dont really need the index, you can use the _ to represent the index
# remember it is not good practise define a variable and never really use it again
"""

for _ in range(3):
    print("meow")
"""

# this is another way to meow 3 times but in 3 separate lines and removes the blank new line at the end
"""
print("meow\n" * 3, end="")
"""
"""
n = int(input("How many times do you want me to meow? "))
while n < 0:
    n = int(input("Please enter a positive number: "))

for _ in range(n):
    print("meow")
"""    
# another way of doing this is to delibeartely induce an infinite loop and break out of it when the condition is met
# this is not a good way to do this but it is possible
"""
while True:
    n = int(input("How many times do you want me to meow? "))
    if n > 0:
        break
    
for _ in range(n):
    print("meow")
  """  
    
# you can use this in a function
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("How many times do you want me to meow? "))
        if n > 0:
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()