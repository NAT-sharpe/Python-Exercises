# num = input('How big is the square? ')

# stars = ''.join('*' for n in range(num))

# for n in range(num):
#         print stars


sides = input('How big is the square? ')
times = 0
char = '*'

while times < sides:
        print char * sides
        times += 1

