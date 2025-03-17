# Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']              # This is a list which is mutable and cannot be a key
{'a': 1, 'b': 2}        # This is a dictionary which is mutable can cannot be a Key.
range(5)
{1, 4, 9, 16, 25}       # This is a set which is mutable and cannot be a key.
3
0.0
frozenset({1, 4, 9, 16, 25})