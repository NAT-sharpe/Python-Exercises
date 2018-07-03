word = "cheese"
long_word = ''

longs = ['e', 'o', 'a']

new_num = 2

pre_letter = ''

for char in word:
    if char == pre_letter and char in longs:
        pre_letter = char
        long_word += char + char * new_num
    else:
        pre_letter = char
        long_word += char

print long_word
