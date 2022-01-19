with open("input7.txt","r", encoding="utf-8") as file:
    lst = [i.strip() for i in file]
    lst1 = " ".join(lst)
print(lst1)
#summ=0
# for i in lst1:
#     if i.isdigit():
#         summ+=int(i)
# print(summ) # суммируются все числа по-отдельности
num=""
for i in lst1:
    if i.isdigit():
        num+=i
    elif num !="":
        print(num)
        num=""
if num !="":
    print(num)




