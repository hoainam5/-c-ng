def to_upper(s):
  result = ""
  for char in s:
    if char >= "a" and char <= "z":
      result += chr(ord(char) - 32)
    else:
      result += char
  return result


print(to_upper("Xin chào"))
def fun(kitu,kitut):
  chuoi_moi=kitu[:10]+kitut
  return chuoi_moi
print(fun("Python is fun","eazy"))

def loai_bo_khoang_trang(chuoi):
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    chuoi = chuoi.strip()

    # Tách chuỗi thành các từ
    tu = chuoi.split()

    # Gắn kết các từ lại với nhau, cách nhau đúng một ký tự trắng
    chuoi_moi = ' '.join(tu)

    return chuoi_moi

tu="       nam đẹp trai  nhất thế   giới  ".split()
chuoi_m = " ".join(tu)
print(chuoi_m)