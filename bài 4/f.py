n=1000
def nt(n):
    if n<2:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

while True:
    n+=1
    if nt(n):
        break
print(n)


    