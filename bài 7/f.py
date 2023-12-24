# Hệ số của phương trình
a1, b1, c1, d1 = 1, 1, 4, 10
a2, b2, c2, d2 = 5, -2, 1, 3
a3, b3, c3, d3 = 1, 1, -3, 5

# Tạo ma trận mở rộng của hệ phương trình
matrix = [
    [a1, b1, c1, d1],
    [a2, b2, c2, d2],
    [a3, b3, c3, d3]
]
rows=len(matrix)
cols=len(matrix[0])
for i in range(rows):
    for j in range(i+1,rows):
        factor = matrix[j][i]/matrix[i][i]
        for k in range(cols):
            matrix[j][k]-=factor * matrix[i][k]
#giải nghiệm
for i in matrix:
    print(i)
z=matrix[2][3]/matrix[2][2]
y=(matrix[1][3]-matrix[1][2]*z)/matrix[1][1]
x=(matrix[0][3]-matrix[0][2]*z-matrix[0][1]*y)/matrix[0][0]
print(x)
print(y)
print(z)
        
solution = [0] * rows
for i in range(rows - 1, -1, -1):
    solution[i] = matrix[i][cols - 1] / matrix[i][i]
    for j in range(i - 1, -1, -1):
        matrix[j][cols - 1] -= matrix[j][i] * solution[i]
print(solution)
'''
for i in range(rows-1,-1,-1):
    a[i]=matrix[i][rows]/matrix[i][i]
    for j in range(i-1,-1,-1):
        matrix[j][rows]-=matrix[j][i]*a[i]
print(a)
'''