bill_input = raw_input("Total bill amount?\n")
bill = float(bill_input)

service = raw_input("Level of service? (good, fair or bad)\n")

tip = 0.00

if service == "good":
    tip = bill * .20
elif service == "fair":
    tip = bill * .15
elif service == "bad":
    tip = bill * .10
else: print "Try again"

grand_total = bill + tip

print "Tip amount: $%.2f" % tip
print "Total amount: $%.2f" % grand_total