import sys

# it is possible to use a try and except block to pick up IndexError that can occur either by:
# not input name at before running or using an index far off

if len(sys.argv) < 2: # name of program is always index 0 and first input is index 1
    sys.exit('too few arguments')
    
for arg in sys.argv[1:]: # this slices the list starting from index 1 as index 0 has the file name
    print('hello, my name is', arg)