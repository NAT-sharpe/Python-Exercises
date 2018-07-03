def create_empty_list(width, height):
    result = []
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result

def add_matrices(m1, m2):
    height = len(m1)
    width =  len(m1[0])
    matrix = create_empty_list(width, height)
    for i in range(0, height):
        for j in range(width):
         matrix[i][j] = m1[i][j] + m2[i][j]
    return matrix

m1 = [
    [1, 3],
    [2, 4]
]

m2 = [
    [5, 2], 
    [1, 0]
]

result = add_matrices(m1, m2)

print result


