# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 
print(text.rfind('f', 21, 35))    # 29  

# line 5 is spliced from [21:35] the lastmost 'f' is the the 8th character of this spliced string.
# line 6 has a starting index of 21 and ending index of 35. since it is not spliced the lastmost 'f'
# is the 28th character of the string.