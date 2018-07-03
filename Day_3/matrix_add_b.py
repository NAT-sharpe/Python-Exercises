box_a = [[1, 3], [2, 4]]
box_b = [[5, 2], [1, 0]]

box_c = []

lst_a = []
lst_b = []

for a in range(len(box_a)):
    for j in box_a[a]:
        lst_a.append(j)
    for k in box_b[a]:
        lst_b.append(k)

for c in range(len(lst_a)):
    num = lst_a[c] + lst_b[c]
    box_c.append(num)

print box_c


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
       r[i][j] = m1[i][j] + m2[i][j]

print r