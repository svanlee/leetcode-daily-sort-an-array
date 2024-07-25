from json import loads
from sys import stdin


# Open a file named 'user.out' in write mode
f = open('user.out', 'w')

# Iterate over the input from the standard input (stdin)
# The map function applies the loads function to each input line
# loads is likely a JSON decoder that converts a JSON string into a Python object (e.g., a list)
for nums in map(loads, stdin):
    # Sort the input list nums
    # Convert the sorted list to a string
    # Remove any spaces from the string
    sorted_nums_str = str(sorted(nums)).replace(' ', '')
    
    # Print the resulting string to the file f
    print(sorted_nums_str, file=f)

# Exit the program with a status code of 0, indicating successful execution
exit(0)