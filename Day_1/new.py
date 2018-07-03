tip_input = raw_input("How much tip? ")

tip = float(tip_input)

bill_input = raw_input("How much bill? ")
bill = float(bill_input)
 

tip_ratio = tip / bill

is_reasonable = tip_ratio >= 0.10 and tip_ratio < .2

if tip < .10:
    print "stingy!"
elif tip > .20:
    print 'generous!'
elif: tip_ratio >= 0.10 and tip_ratio < .2
    print 'is_reasonable'
else: print 'wierd!'