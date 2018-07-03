height = input('Height? ')

width = (height * 2) - 1

star = '*'

print star.center(width)

for i in range(height - 1):
    star = ''.join('*') + star + ''.join('*')
    print star.center(width)

