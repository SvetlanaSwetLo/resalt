#               # СПИСКИ
# lst=[1,3.5, "hello", True]
# lst1=["rrrrr","yyyyyyy"]
# lst[0]=35 #замена по индексу
# print(lst)
# lst.append("ppppppp") #длобавляем элемент в конец списка
# print(lst)
# lst.insert(2, False) # замена по указанному индексу
# print(lst)
# lst.extend(lst1) # расширяет саписок за счет другого
# print(lst)
# print(lst+lst1) # сложение списков
# print(lst*2) #умножение на число
# lst.remove(35) # удаляет по значению
# print(lst)
# del lst[1] # удаляет по указанному индексу
# print(lst)
# d=lst.pop(3) # удаляет и записывает в переменную
# print(lst)
# print(d)
# lst.reverse() # разворачивает список
# print(lst)
# lst2=[1,8.9,15,0,33]
# lst2.sort() # сортирует по возростанию цифры или по алфавиту буквы
# print(lst2)
# lst3=sorted(lst2) # создает отсортированную копию списка
# print(lst3)
# s=lst3.index(15) # выводит индекс первого вхождения значения
# print(s)
# print(lst3)
# lst5="455 414 877 7 9"
# lst4=lst5.split(" ") # разбивает строку на список строк по указанному разделителю
# print(lst4)
# lst6=["hgg","455","vyfft","478445"]
# lst6="$$$$$$".join(lst6) # объединяет списки в строку с указанным разделителем
# print(lst6)
#          # КАРТЕЖИ
# lst7=[7,8.9,78,[7,99999,"iuyg"]]
# y=tuple(lst7)
# print(y)
# print(type(y))
# y[3][2]=565
# print(y)
#        # ФАЙЛЫ
#
# # with open("input8.txt", "r",encoding="utf-8") as file: # только для чтения
# #     print(file.read())
# # with open("input9.txt", "w",encoding="utf-8") as file: # перезаписать файл, если файла с таким именем нет, то создаст и запишет, что указанно в "
# #     print(file.write("fgfgfghhgfgfhg"))
# # with open("input8.txt", "a",encoding="utf-8") as file: # дозаписывает в указанный файл, то что в ковычках
# #     print(file.write(" Ура"))
# # with open("../ee.txt", "r",encoding="utf-8") as file: # только для чтения
# #     print(file.read())
# lst10=s[1,8,10]
# Задача 1
lst=[8,"ttt",1,"ttt",7,True,8,True,"ddd",3]
print(lst)
res=[]
for i in lst:
     if lst.count(i)==1:
         res.append(i)
print(res)