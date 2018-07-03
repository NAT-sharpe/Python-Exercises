width = input('Width? ')

height = input('Height? ')

top_bottom = ''.join('*' for w in range(width))

print top_bottom

sides = '*' + ''.join(' ' for w in range(width - 2)) + '*'

for h in range(height - 2):
        print sides

print top_bottom


# if first row or last row or first column or last column

#loops in loops