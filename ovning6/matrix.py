def eye(n):
    template = [0 for i in range(n)]
    matrix = []
    for i in range(n):
        row = template[:]
        row[i] = 1
        matrix.append(row)
    return matrix

mat = eye(1)
for row in mat:
    print(row)
print(mat)
