bill = float(raw_input("Total bill amount?\n"))

service = raw_input("Level of service?\n")

tip = 0.00

if service == "good":
    tip = bill * .20
elif service == "fair":
    tip = bill * .15
elif service == "bad":
    tip = bill * .10
else: 
    try_again = raw_input("Please enter \'good,\' \'fair\' or \'bad:\'\n")
    if try_again == "good":
        tip = bill * .20
    elif try_again == "fair":
        tip = bill * .15
    elif try_again == "bad":
        tip = bill * .10

people_input = float(raw_input("Split how many ways?\n"))

grand_total = bill + tip
split = grand_total / people

round(split, 2)

print "Tip amount: $%.2f" % tip
print "Total amount: $%.2f" % grand_total
print "Amount per person: $%.2f" % split