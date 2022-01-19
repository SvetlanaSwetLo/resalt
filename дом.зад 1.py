lst=[]
with open ("input1.txt","r", encoding="utf-8") as file: #считываем построчно
    lst=[i.strip().split() for i in file]
print(lst)
s=0
# k=0
    for i in lst:
        s+=int(i[2])
print(s)




