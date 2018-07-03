num = input("Factor what number? ")
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print "The factors of %s are:" % num
print factors[0:]


