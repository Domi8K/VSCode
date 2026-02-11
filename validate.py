import re

email = input("What's your email? ").strip()

# . means any character except a newline, * means 0 or more repetitions, + means 1 or more repetitions
# ? means 0 or 1 repetition, {m} means m repetitions, {m,n} means m to n repetitions
# ..* has same effect as .+
# re.search('.+@.+.edu', email) looks at that string ends with edu as . means something else
# re.search(r'.+@.+\.edu', email) does exactly as we want (asserts that email entered ends with .edu), 
# of course changing the \. to \? only accepts emails that end with ?edu
# using \ then a special characters means literally that one character has to follow after \
# having re.search(r'^.+@.+\?edu$', email) means the string starts with from ^ and ends at $ exclusive
# re.search(r'^[^@]+@[^@]+\?edu$', email) partly means one or more characters (on the left)  that are NOT in the set, in this case '@' 
# while just a regular [] (without ^)  means only characters within that set should be given
# re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\?edu$', email) means only a to z AND capitals AND 0 to 9 and a underscore (_) will be accepted
# \w has same effect as [a-zA-Z0-9_]
# \d = decimal digit \D = NOT a decimal digit \s = whitespace character \S = NOT whitespace character \w = alphanumeric characte and _ 
# /W = NOT alphanumeric or _
# A|B means either A or B, (...) means a group, (?:...) means a non caputring version
if re.search(r'^(\w|\.)+@(\w+\.)*\w+\.(com|edu|org|gov|net)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')