letters_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                                't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_n(n):
    return letters_array[n]

print find_n(5)

# Find even items in a list


def find_even(array):
    new_list = [a for i, a in enumerate(array, 1) if i % 2 == 0]
    return new_list

print find_even(letters_array)

# Find odd items in a list


def find_odd(array):
    new_list = [a for i, a in enumerate(array, 1) if i % 2 == 1]
    return new_list

print find_odd(letters_array)
