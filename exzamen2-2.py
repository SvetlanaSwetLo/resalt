# # Задача 1
# lst=[8,"ttt",1,"ttt",7,False,8,99,"ddd",3]
# print(lst)
# res=[]
# for i in lst:
#       if lst.count(i)==1:
#           res.append(i)
# print(res)
# Задача 2
lst=[45,45,45,45,45,45,45]
res=[]
kol=0
kol1=0
for i in lst:
      if lst.count(i)%2==0:
        kol+=1
        res.append(i)
      elif lst.count(i) % 2 == 1 and lst.count(i) > 1:
        kol1+=0.5
        res.append(i)
print(res)
print(f'Количество пар = {round((kol+kol1)/2)}')
