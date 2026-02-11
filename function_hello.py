# A simple function that takes a parameter and prints a greeting
def hello():
    print("Hello, ")


name = input("What is your name? ")
hello()
print(name)

# a better way would be to create a function that takes a parameter
# and then call that function with the name as the argument
def hello(to):
    print("Hello, ", to)
    
name = input("What is your name? ")
hello(name)

# a default value can be provided for the parameter if the user does not provide a value
# this only works if there is no initial input of name
def hello(to="friend"):
    print("Hello, ", to)
    
hello()

# the next line would with the name entered included
name = input("What is your name? ")
hello(name)

# using the main function
def main():
    name = input("What is your name? ")
    hello(name)
    
def hello(to="friend"):
    print("Hello, ", to)
    
main()