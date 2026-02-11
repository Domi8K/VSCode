# Ask the user for their name
name = input("What is your name? ")

# Print a greeting
print("Hello, " + name + "!")

print("Hello, ", end="")
print(name)

print("Hello, ", name, sep="????")

print("Hello,", name)

print('Hello, "friend :}"')
print("Hello, \"friend\"")

print(f"Hello, {name}")

# Remove leading and trailing whitespace
name = name.strip()
print(f"Hello, {name}")

# Capitalizes user's name
name = name.capitalize()
print(f"Hello, {name}")

# Capitalizes user's names
name = name.title()
print("Hello, " + name)

# remove leading and trailing whitespace and capitalize user's names
name = name.strip().title()
print("Hello, " + name)

# ask the user for their name and remove leading and trailing whitespace and capitalize user's names
name = input("What is your name? ").strip().title()
print("Hello, " + name)

# Split the user's name into first and last names
first, last = name.split(" ")
print(f"Hello, {first}")