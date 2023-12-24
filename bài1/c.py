n=0
tong=0
while True:
    n+=1
    tong+=(n-1)/(n+1)
    if tong>=100:
        tong-=(n-1)/(n+1)

        n-=1
        break
print(n)
print(tong)