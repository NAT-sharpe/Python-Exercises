today_seats = [
    'Tracy',
    'Nat',
    'Will',
    'Brandon'
]

yesterdays_seats = [
    'Tracy',
    'Nat',
    'Brandon',
    'Will'  
]

for i in range(len(today_seats)):
    if today_seats[i] == yesterdays_seats[i]:
        print "Move %s!" % today_seats[i]

i = 0

while i < len(today_seats):
    if today_seats[i] == yesterdays_seats[i]:
        print "Move %s!" % today_seats[i]
    i += 1

# for loops let you step thru lists with known length
# use while loop when you don't know how long you'll be looping

#best:
for student in today_seats:
    print student
#same as:
i = 0
while i < len(today_seats):
    print today_seats[i]
    i = i + i
#same as:
for i in range(len(today_seats)):
    print today_seats[i]
