# this is about lists
"""
students = ["Hermione", "Harry", "Ron", "Luna"]
print(students[3])
"""
# you can use a for loop to iterate through the list
"""
for student in students:
    print(student)
 """
    
# you can also use the range function to iterate through the list
"""
for i in range(len(students)):
    print(i, students[i])
    
"""
# other than lists you can use dictionaries
# dictionaries are key value pairs

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Luna": "Ravenclaw"
    }
print(students["Ron"])

# you can loop it by

for student in students: # when using a dictionary, it will only loop through the keys
    # print(student) will only print out the keys
    print(student, students[student], sep=", ") # this will print out the key value pairs
    
# you can also use the items method to loop through the dictionary
# this will return a tuple of the key value pairs
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russell Terrier"},
    {"name": "Luna", "house": "Ravenclaw", "patronous": "hare"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")