n=0
while True:
    try:
        m=int(input('nhập giá trị m\n'))
        break
    except:
        print('nhập lại giá trị')
tong=0
while tong<=m:
    n+=1
    tong+=n**2
print(n)
print(tong)