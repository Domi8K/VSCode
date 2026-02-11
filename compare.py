x = int(input("What is the value of x? "))
y = int(input("What is the value of y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")
    
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")