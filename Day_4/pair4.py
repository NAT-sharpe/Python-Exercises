msg = raw_input('msg:')

word_histogram = {}

entry = ''

for char in msg:
    if char != ' ':
        entry = entry + char
    elif char == ' ':
        break

word_histogram[entry] = 0


print entry
print word_histogram