text = raw_input('Text? ')
length = len(text) + 4
char = '*'

top_bottom = char * length
middle = '%s %s %s' % (char, text, char)

print top_bottom
print middle
print top_bottom