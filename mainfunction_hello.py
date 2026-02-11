def main():
    name = input("What is your name?")
    hello(name)
    

def hello(to="world"):
    print("hello,", to)
    
 # by calling the function main() we can run the code in the 'main' function that is then passed to the 'hello' function   
main()   

"""
def main():
    name = input("What is your name?")
    hello()
    
def hello():
    print("hello,", name)
"""
# this code will not work as the 'name' variable is not defined in the 'hello' function, it only exists in the 'main' function
# to fix this we can pass the 'name' variable as an argument to the 'hello' function
# in the first example we have done this by passing the 'name' variable as an argument to the 'hello' function
# however the 'name' variable has a different name in the 'hello' function, it is called 'to' in the 'hello' function