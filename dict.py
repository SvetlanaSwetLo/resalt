#data={
#    'fname':'lena',
#    'lname':'moron'
#}
#data['nomber']="+37529" # добавляем ключ-значение в словарь
#print(data)
#print(data.get('pol', "GFFH")) # выводим значение по ключу, если нет то пишет GFFH или то что захочешь
#print(data.setdefault("nom","ytn")) # то же что и  get, не понимаю разницу
#del data["lname"] # удаляет насовсем ключ и значение
#ret=data.popitem() # удаляет в новую переменную ret картежем ключ и значение
#data1={
   #
#
#for values in data.values(): # итерирует по значениям(values)
#    print(values)
#for keys in data.keys(): # итерирует по ключам
#    print(keys)
#for items in data.items(): # итерирует по ключам-значениям, выводит их ввиде картежей
#    print(items)
#print(list(data.items())) #выводит списком ключ-значение

# Задача 1
# a=int(input("введите первое число "))
# b=int(input("введите второе число "))
# data={}
# for i in range(a, b+1):
#     data[i]=i**3
# print(data)

# Задача 2
# даны 2 списка одинаковой длины. Сщздать словарь, что бы элементы первого списка являлись ключами,
# а элементы второго - значениями
#lst=[3,8,5, "bggg"]
#lst1=["vf","hyu","895","pokjbvv"]
#data={}
#for i in range(len(lst)):
#    data[lst[i]]=lst1[i]
#print(data)

#задача 3
#lst="hello world"
#data={}
#for i in lst:
#    data[i]=lst.count(i)
#print(data)

#quiz={input('Question: '.title():input('Answer: '.title() for i in range(int(input('how much?')))}
#print(quiz)
quiz={}
while True:
    question=input('Question: ').title()
    answer=input('Answer: ').title()
    if question!='exit' and answer!='exit':
        quiz[question]=answer
    else:
        break
total=0
for question,right_answer in quiz.items():
    print(question, end=' ')
    answer=input().title()
    if answer==right_answer:
        total+=1
    print('*'*10)
print(f'{total} из {len(quiz)}')