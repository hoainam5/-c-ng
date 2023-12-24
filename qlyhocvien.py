import csv 
f=open('Files/diemcc.csv','r+',encoding='utf-8')
print(f)
data=list(csv.reader(f,delimiter=';'))
for i in range(1,len(data)):
    if float(data[i][6])>=8:
        data[i][7]='Giỏi'
    else:
        data[i][7]='Non'

def in_bang_du_lieu(danh_sach_2d):
    for hang in danh_sach_2d:
        for gia_tri in hang:
            print(gia_tri.ljust(15), end="")  # Sử dụng ljust để căn lề trái và tạo khoảng cách
        print()

# In bảng dữ liệu
in_bang_du_lieu(data)
f.seek(0)
writer = csv.writer(f,delimiter=';',lineterminator='\n')
writer.writerows(data)
f.close()
'''
f.seek(0)
writer = csv.writer(f,delimiter=';',lineterminator='\n')
writer.writerows(data)
f.close()'''