m1 = [
    [1, 3],
    [2, 4]
]

m2 = [
    [5, 2], 
    [1, 0]
]

r = []

for row in m1:
    wip = []
    for column in row:
        wip.append(0)
    r.append(wip)

width =  len(r[0])
height = len(r)

for i in range(height):
    for j in range(width):
       r[i][j] = m1[i][j] * m2[i][j]

print r