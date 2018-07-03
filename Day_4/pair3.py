msg = raw_input('msg:')

letter_histogram = {}

for char in msg:
    if char in letter_histogram:
        letter_histogram[char] += 1

    else:
        letter_histogram[char] = 1


print letter_histogram
