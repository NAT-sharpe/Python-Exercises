message = "storm the castle!"

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_string = ""

pre_letter = ' '

for char in message:
    if pre_letter == ' ':
        pre_letter = char
        for i in range(len(lowercase)):
            letter = lowercase[i]
            if letter == char:
                char = uppercase[i]
                pre_letter = char
                break
        new_string = new_string + char
    else:
        pre_letter = char
        new_string = new_string + char

print new_string
