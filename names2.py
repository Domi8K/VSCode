# this reads from a file
names = []

with open('names.txt', 'r') as file: # implicitly, open('names.txt') will also open for read
    """
    lines = file.readlines()
    for line in lines:
        print('hello', line.rstrip())
    """
    for line in file: # for line in sorted(file) also sorts the file
        names.append(line.rstrip())
        # print('hello,', line.rstrip()) # rstrip() removes new lines from the open file
        
for name in sorted(names, reverse=True):
    print(f'hello, {name}')