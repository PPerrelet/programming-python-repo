my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal?
    # Yes my_list and another_list are equal. They contain the same elements.
# Are the lists assigned to my_list and another_list the same object?
    # They are not the same object. list() causes a shallow copy. 
# Are the nested lists at index 3 of my_list and another_list equal?
    # They are equal.
# Are the nested lists at index 3 of my_list and another_list the same object?
    # They are the same. Shallow copies only reference NESTED lists.

# Shallow copies will create a new object for a new list. However it will only refence a nested list. 