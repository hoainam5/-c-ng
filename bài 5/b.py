# Tạo danh sách các số lẻ
so_le = [1, 3, 5, 7, 9]

# Nối các số lẻ trong danh sách thành một chuỗi
chuoi_so_le = ",".join(str(so) for so in range(1000,30000+1) if so%2!=0)

# In chuỗi ra màn hình
print(chuoi_so_le)

def tinh_so_tien_rut(von, lai_suat_thang, so_thang):
    for thang in range(1, so_thang + 1):
        von = von * (1 + lai_suat_thang / 100)
    
    return von

# Nhập dữ liệu từ bàn phím
von = float(input('Nhập số tiền gửi ban đầu: '))
lai_suat_thang = float(input('Nhập lãi suất hàng tháng (%): '))
so_thang = int(input('Nhập số tháng gửi tiền: '))

# Gọi hàm để tính và in ra số tiền rút được sau n tháng
ket_qua = tinh_so_tien_rut(von, lai_suat_thang, so_thang)
print(f'Số tiền rút được sau {so_thang} tháng là: {ket_qua:.5f} đồng')
