k=''
while True:
    i=input('nhập kí tự:\n')
    if i=='*':
        break
    else:
        k+=i
tong=0
for i in k:
    if i.isnumeric():
        tong+=int(i)