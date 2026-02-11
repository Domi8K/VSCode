name = input("What is your name? ")

"""	
if name == "Mpho":
    print("Ramolefhe")
elif name == "Refilwe":
    print("Ramolefhe")
elif name == "Peter":
    print("Ramolefhe")
elif name == "Katlego":
    print("Ramolefhe")
elif name == "Clifford":
    print("Charlie")
else: 
    print("You are not allowed to enter the room.")
"""

# a more efficient way to write the code
"""
if name == "Mpho" or name == "Refilwe" or name == "Peter" or name == "Katlego":
    print("Ramolefhe")
elif name == "Clifford":
    print("Charlie")
else: 
    print("You are not allowed to enter the room.")
"""

# a shorter way is to use the matching operator
match name:
    case "Mpho" | "Refilwe" | "Peter" | "Katlego": # the longer more straightforward way is to case each name separately
        print("Ramolefhe")
    case "Clifford":
        print("Charlie")
    case _:
            print("You are not allowed to enter the room.")
