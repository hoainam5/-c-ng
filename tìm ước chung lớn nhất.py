def ucln(a,b):
    if b==0:
        return a
    return ucln(b,a%b)
print(ucln(1001,1001))
def bcnn(a,b):
    bcn=(a*b)/ucln(a,b)
    return bcn
print(bcnn(100,20))