# Hệ số của phương trình
a1, b1, c1 = 2, 3, 7
a2, b2, c2 = 1, -1, 1
n=a2/a1

# Nhân hệ số của phương trình thứ nhất
a1, b1, c1 = n*a1, n*b1, n*c1

# Lùi bước phương trình thứ nhất trừ đi phương trình thứ hai
a1, b1, c1 = a1 - a2, b1 - b2, c1 - c2

# Giải phương trình thu được để tìm giá trị của y
y = c1 / b1

# Thay giá trị y vào phương trình để tìm giá trị của x
x = (c2 - b2*y) / a2

# In kết quả
print("Giá trị của x là:", x)
print("Giá trị của y là:", y)
