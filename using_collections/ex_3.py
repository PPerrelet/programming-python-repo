# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original.
# It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

seq = ((1, 2, 3, 4, 5)[::-1][1:4])

print(seq)