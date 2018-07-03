box_a = [[1, 3, 5], [3, 2, 6], [2, 3, 4]]
box_b = [[5, 7, 2], [4, 2, 9], [1, 0, 5]]

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
   

