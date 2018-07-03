lst1 = [
    10,
    5,
    3,
    6
]

lst2 = [
    3,
    2,
    5,
    1 
]

lst3 = []

for i in range(len(lst1)):
    prod = lst1[i] * lst2[i]
    lst3.append(prod)
print "%sX%s=%s" % (lst1, lst2, lst3)