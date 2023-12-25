def snt(n):
    a=[True]*(n+1)
    a[0]=a[1]=False
    for i in range(2,int(n)+1):
        if a[i]:
            for j in range(i*i,n+1,i):
                a[j]=False
    nt=[i for i in range(n) if a[i]]
    return nt
print(snt(100000))