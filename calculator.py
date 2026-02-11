x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
# the above will concatinate x and y as strings

# to add them as numbers, we need to convert them to integers
z = int(x) + int(y)
print(z)

# a shorter way is
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

# this converts string to floating point values or more commonly known as a float or decimal
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# this will round the sum of x and y to the nearest whole number
print(round(x + y))
print(f"{round(x + y)}")

# this will add a comma to the number to make it more readable
z = (x + y)

print(f"{z:,}")

# this will round to 4 decimal places
a = (x / y, 4)

print(a)

# you can also use the format method to round to 4 decimal places

print(f"{a:.4f}")