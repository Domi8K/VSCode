import re

name = input('What is your name? ').strip()
if matches := re.search(r'^(.+), *(.+)$', name): # paranthesis () capture data meaning it will be returned as a group;
# ? stands with the space char to show 0 or 1 repetitions or the character
# := allows us to assign a value and ask a boolean question at the same time

    last, first = matches.groups() # similar is last = matches.group(1) first = matches.group(2)
    name = f'{first} {last}' # cleaner is name = matches.group(2) + ' ' + matches.group(1)
print(f'hello, {name}')