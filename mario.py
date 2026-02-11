def main():
    columns = column()
    rows = row()
    size = square_size()
    print_column(columns)
    print_row(rows)
    print_square(size)
    
def square_size():
    while True:
        size = int(input("How big do you want the square to be? "))
        if size > 0:
            return size
        
def print_square(size):
    for _ in range(size): # for each row of the square
        print("@" * size)
def row():
    while True:
        numberRow = int(input("How many rows do you want? "))
        if numberRow > 0:
            return numberRow

def print_row(width):
    print("?" * width)
    
def column():
    while True:
        number = int(input("How many columns do you want? "))
        if number > 0:
            return number

def print_column(height):
    print("#\n" * height, end="")
        
main()