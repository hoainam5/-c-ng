n = int(input())

def hoan_hao(n):
 
    if n <=0:
        return False
        print('vui lòng nhập số dương')
    tong = 0
    for i in range(1,n):
        if n % i ==0:
            tong +=i
    if tong == n:
            return True
    else:
        return False
    
def gan_nhat(n):
    if hoan_hao(n):
        return n
    m = n + 1
    while True:
        if hoan_hao(m) and m - n > 100:
            return m
        m += 1

result = gan_nhat(n)
print(gan_nhat(n))
