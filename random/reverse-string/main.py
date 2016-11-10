string = 'oompaloompa'

# First Example
# http://stackoverflow.com/questions/931092/reverse-a-string-in-python

reversed_string = string[::-1]

print 'First Example: ', reversed_string

# Second Example

reversed_string = ''

for s in reversed(string):
    reversed_string += s

print 'Second Example: ', reversed_string
