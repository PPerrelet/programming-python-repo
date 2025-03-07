# Which of the identifiers in the following program are function names?
# say

# Which are method names? 
# upper, lower

# Which are built-in functions?
# print, input, max

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))