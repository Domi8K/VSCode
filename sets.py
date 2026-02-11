# create an empty set
s = set()

for i in range (10):
    s.add(i +1)
    
print(s)

for i in range (3):
    s.remove(i+1)
    
print(s, len(s))