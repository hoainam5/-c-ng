# sang nt
def snt(n):
    a=[True]*(n+1)
    a[1]=a[0]=False
    for i in range(2,n+1):
        if a[i]:
            for j in range(i*i,n+1,i):
                a[j]=False
    return a
for i in range(101):
    if snt(100)[i]== True:
        print(i)
