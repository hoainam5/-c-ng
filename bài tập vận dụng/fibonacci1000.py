def fbnc(n):
    a=[0,1]
    while True:
        fibonacci=a[-1]+a[-2]
        if fibonacci>=n:
            break
        a.append(fibonacci)
    return a
print(fbnc(1000))