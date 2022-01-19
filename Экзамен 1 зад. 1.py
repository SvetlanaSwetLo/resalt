a=input('Введите семизначное число:')
chet=0
nchet=0
for i in a:
    if int(i)%2==0 and len(a)==7:
        chet+=1
    elif len(a)!=7:
        print("Ошибка")
    else:
         nchet+=1
print(chet)
print(nchet)
s=0
p=1
for i in range(len(a)):
    if chet>nchet:
        s+=int(a[i])
    else:
        p=int(a[0])*int(a[2])*int(a[5])
print(s)
print(p)