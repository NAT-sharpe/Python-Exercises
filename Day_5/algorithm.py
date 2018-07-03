factor = 1
giant = 150

while giant > factor:
    factor += 1
    while giant % factor == 0:
        giant = giant / factor

print factor


number = 600851475143

remainder = number
factor = 2

while remainder != 1:
    if remainder % factor == 0:
        remainder /= factor
    else:
        factor += 1