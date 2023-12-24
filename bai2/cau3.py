k=''
while True:
    i=input('nhập kí tự:\n')
    if i=='*':
        break
    else:
        k+=i
b=k[0].upper() + k[1:]
print(b)