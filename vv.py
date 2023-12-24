import csv

# Tạo một đối tượng writer
csv_writer = csv.writer(open('example.csv', 'w', newline=''))

# Sử dụng hàm dir() để liệt kê tất cả các thuộc tính và phương thức của đối tượng
attributes = dir(csv_writer)

# In tất cả các thuộc tính và phương thức
for attribute in attributes:
    print(attribute)
print(dir())