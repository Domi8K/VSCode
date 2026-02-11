def main():
    x = input('Enter a number: ')
    print(f'the square of {x} is', square(x))
    
def square(n):
    return n * n

if __name__ == '__main__':
    main()