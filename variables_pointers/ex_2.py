# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1 # set2 points to the same place in memory as set1. this is just a reference assignment
set1.add(range(5, 10))
print(set2)
print(set2 == set1)
print(set2 is set1)