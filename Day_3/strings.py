string = "storm the CASTLE!"

new_string = ""

lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in string:
    if char in lower:
        for j in range(len(lower)):
            if char == lower[j]:
                new_string += upper[j]
                break
    else:
        new_string += char

print new_string

new_string = ""

# Jonathan's version below:

for char in string:
    for i in range(len(lower)):
        lowerletter = lower[i]
        if lowerletter == char:
            char = upper[i]
            break

    new_string = new_string + char

print new_string

        