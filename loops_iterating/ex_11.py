# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):  # Loop through the outer list
    nest_index = 0
    while nest_index < len(my_list[index]):  # Loop through the inner lists
        if my_list[index][nest_index] % 2 == 0:  # Check if the number is even
            print(my_list[index][nest_index])  # Print the even number
        nest_index += 1  # Increment the inner index
    index += 1