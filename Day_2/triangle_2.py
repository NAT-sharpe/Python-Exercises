
# star = '*'

# print star.center(width)

# for i in range(height - 1):
#     star = ''.join('*') + star + ''.join('*')
#     print star.center(width)

# height = input('Height? ')

# width = (height * 2) - 1

number_of_layers = input('Height? ')

space = '_'
space_number = number_of_layers - 1

char = '*'
char_number = char

for num in range(number_of_layers):
    print space * space_number + char_number + space * space_number 
    space_number -= 1
    char_number += char * 2

