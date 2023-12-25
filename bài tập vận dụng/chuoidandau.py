g=0
n=1000
for i in range(1,n+1):
    if i%2!=0:
        g+=1/i
    else:
        g-=1/i
print(g)