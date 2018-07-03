string_input = raw_input('Count words in: ')

# Turn string_input into lowercase with no special characters:

string = '' 

lower = " 'abcdefghijklmnopqrstuvwxyz"
upper = " 'ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in string_input:
    if char in upper:
        for j in range(len(upper)):
            if char == upper[j]:
                string += lower[j]
                break
    elif char in lower:
        string += char

# Find words in string and place into temp_list:



padded_string = string + ' '

# for i in range(len(string)):
#     while string[i] != ' ' # and i < len(string):
#         entry += string[i]
#         if i == len(string) - 1:
#             temp_list.append(entry)
#         break
#     else:
#         temp_list.append(entry)
#         entry = ''

words = []
curr_word = ''

for char in padded_string:
    if char == ' ':
        words.append(curr_word)
        curr_word = ''
    else:
        curr_word += char

# Count each word in temp_list and add to histogram:

histogram = {}

for word in words:
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1

print
print histogram
print
