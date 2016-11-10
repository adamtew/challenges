array = ['1', '2', '3', '4', '5', '6']

# First Example

reversed_array = array[::-1]
print 'First Example: ', reversed_array

# Second Example

reversed_array = []

for a, b in enumerate(reversed(array)):
    reversed_array.append(b)

print 'Second Example: ', reversed_array
