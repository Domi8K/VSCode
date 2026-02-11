# this creates a library to be reused in another file

def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f'hello, {name}')
    
def goodbye(name):
    print(f'goodbye, {name}')
    
# do not call main() as it would cause this whole file to be read and printed when being called in another program ...
# ... even though you only wanted a specific part, say maybe hello funtion or goodbye function
# however if you want this whole program to run by calling main() in a different program then:

if __name__ == '__main__':
    main()