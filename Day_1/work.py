day = int(raw_input('Day (0-6)? '))


if day == 0 or day == 7:
    print "Sleep in"
elif day >= 1 and day <=6:
    print "Go to work"
else:
    print "Try again"