def dx(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
n=100
m=0
for i in range(n-1,n-50,-1):
    if dx(i):
        m=i
print(m)