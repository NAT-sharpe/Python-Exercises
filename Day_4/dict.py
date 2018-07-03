# phonebook = {
#     'Jon': '890011',
#     'Mark': '228902',
# }

# # similar to list of tuples but easier to access:
# # all arrays have keys but are just 0,1,2, etc.

# phonebook = [
#     ('Jon', '890011')
#     ('Mark', '228902')
# ]

# phonebook = {
#     'Jon': '890011',
#     'Mark': '228902',
# }

# phonebook['Brandon'] = '2892020'

# print phonebook

# driver is tactical
# navigator is strategic

string = "You shall not pass!"

new_string = ""

letter_mapping = {
    "a": "A",
   "b": "B",
   "c": "C",
   "d": "D",
   "e": "E",
   "f": "F",
   "g": "G",
   "h": "H",
   "i": "I",
   "j": "J",
   "k": "K",
   "l": "L",
   "m": "M",
   "n": "N",
   "o": "O",
   "p": "P",
   "q": "Q",
   "r": "R",
   "s": "S",
   "t": "T",
   "u": "U",
   "v": "V",
   "w": "W",
   "x": "X",
   "y": "Y",
   "z": "Z"
}

for char in string:
    letter = char

    if char in letter_mapping:
        letter = letter_mapping[char]

    new_string = new_string + letter

print new_string

        