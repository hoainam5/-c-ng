k=''
while True:
    i=input('nhập kí tự:\n')
    if i=='*':
        break
    else:
        k+=i
b=k[::-1]

print('chuỗi ban đầu',k)
print('chuỗi sau khi đảo ngược',b)
m=0
n=''
for i in k:
    if m< k.count(i):
        m=k.count(i)
        n=i
print(n,'xuất hiện nhiều nhất')
