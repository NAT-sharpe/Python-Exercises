message = "Lbh zhfg hayrnea jung lbh unir yrnearq."

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = 13

solution = ""

for char in message:
    if char in lowercase or char in uppercase:
        for i in range(len(lowercase)):
            if char == lowercase[i]:
                letter = lowercase[(i + num) % 26]
                # letter = lowercase[i - num]
                solution += letter
                break
            elif char == uppercase[i]:
                letter = uppercase[(i + num) % 26]
                # letter = uppercase[i - num]
                solution += letter
                break
    else:
        solution += char

print
print solution
print