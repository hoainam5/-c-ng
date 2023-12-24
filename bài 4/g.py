def chinh_phuong(n):
    if (n**(1/2))**2==n:
        return True
    return False
n=100
while True:
    n-=1
    if chinh_phuong(n):
        break
print(n)