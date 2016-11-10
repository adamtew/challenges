string = 'AABBCKLJSDFOISDFJLSKDFJSDFMNSLDKFJSIDOF'
characters = 'AEIOUY'

print 'String: ', string

# Second example

vowel_positions = [i for i, s in enumerate(string) if s in characters]

minimum_jump_ability = i = 0

for i in range(1, len(vowel_positions)):
    difference = abs(vowel_positions[i] - vowel_positions[i - 1])
    if difference > minimum_jump_ability:
        minimum_jump_ability = difference

print 'first example: ', minimum_jump_ability


# First example

minimum_jump_ability = i = 0


for s in string:
    i += 1
    if s in characters:
        if i > minimum_jump_ability:
            minimum_jump_ability = i
        i = 0

print 'second example: ', minimum_jump_ability
