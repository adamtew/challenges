letters_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                                't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_n(n):
    return letters_array[n]

print find_n(5)

# Find even items in a list


def find_even(array):
    return [a for i, a in enumerate(array, 1) if i % 2 == 0]

print find_even(letters_array)

# Find odd items in a list


def find_odd(array):
    return [a for i, a in enumerate(array, 1) if i % 2 == 1]

print find_odd(letters_array)

# Find middle value position

value_array = [0, 8, 3, 4, 12, 6, 6, 10, 6, 5, 4, 2]
value_array = [0, 1, 0, 0, 0, 0, 0]


def find_middle_value(array):
    total = sum(array)
    middle_value = 0
    for i, x in enumerate(array):
        print x, i
        middle_value += array[i]
        if middle_value == total / 2:
            return i
    return None

print find_middle_value(value_array)


