text = raw_input('Text? ')

top_bottom = ''.join('*' for w in range(len(text) + 4))

middle = '* ' + ''.join(text) + ' *'

print top_bottom
print middle
print top_bottom