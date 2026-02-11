"""
This program determines whether a number is even or odd.

x = int(input("What is the value of x? "))

# determing whether x is even or odd

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
"""	

def main():
    x = int(input("What is the value of x? "))

    # determing whether x is even or odd

    if is_even(x): # this can be seen as {if is_even(x) == True:} which is more understandable
       print("x is even")
    else:
       print("x is odd")
       
#def is_even(n):
    #if n % 2 == 0:
     #   return True
    #else:
     #   return False
     
     
# a pythonic way to write the function is
def is_even(n):
    
    # return True if n % 2 == 0 else False
    
    #the above line can be written more efficiently as
    return n % 2 == 0
 

main()