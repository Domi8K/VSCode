def main():
    x = int(input("What's x?"))
    print("x squared is", square(x)) # but square is not defined yet so define it
    

def square(n):
    return n * n # will return the square of n which n would be x from the main function
    # return n ** 2 which is another way to return the square of n
    # return pow(n, 2) which is another way to return the square of n


main ()