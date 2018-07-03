height = 4
character = '*'
space = height * ' '

for i in range(height):
    print space *  + character
    character += '**'
    height -= 1