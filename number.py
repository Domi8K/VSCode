def main():
    x = get_int('What is x? ')
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt)) # this can be simplified to one line; return int(input('What is x? '))
            return x
            # break <-- would also work fine; you can remove the else: break in line 7 & 8
        except ValueError:
            pass
            # print('x is not an integer')
        # else:   
            # return x # break here works if you do not need to return a value

main()