star = '*'

print star.center(7)

for i in range(3):
    star = ''.join('*') + star + ''.join('*')
    print star.center(7)
