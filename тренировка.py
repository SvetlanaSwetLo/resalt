# file=open("input.txt","r", encoding="utf-8")
# lst=[]
# for i in file:
#     lst.append(int(i.strip()))
# print(lst)
#     #lst=[int(i.strip()) for i in file]
# s=sum(lst)
# print(s)
# with open("output3.txt","w", encoding="utf-8") as file:
#       file.write(str(s))
# Задача 2
# with open("input1.txt","r", encoding="utf-8") as file:
#     lst=[i.strip() for i in file]
# print(lst)
# res=[]
# for i,j in enumerate(lst):
#     count_word=j.count(" ")+1
#     count_letter=0
#     for k in j:
#         if k.isalpha():
#             count_letter+=1
#     text=(f"В {i+1} строке: {count_word} слова, {count_letter} букв")
#     res.append(text)
#     print(f"В {i+1} строке: {count_word} слова, {count_letter} букв")
# with open("output4.txt","w", encoding="utf-8") as file:
#     file.write("\n".join(res))
#Задача 3
# with open("input3.txt", "r", encoding="utf-8") as file:
#     students=[i.strip().split() for i in file]
# print(students)
# s=0
# bad_students=[]
# for student in students:
#     s+=int(student[2])
#     if int(student[2])<=3:
#         bad_students.append(student[1])
# s=s/len(students)
# with open("input5.txt", "w", encoding="utf-8") as file:
#     file.write(f"средний бал {s},двоечники: {bad_students}")
import os

print(os.name)
print(os.getlogin())
print(os.getcwd())
print(os.listdir("."))
#os.mkdir("gfgrf")
#os. makedirs('folder/tttt')
#os.rename("gfgrf","folder2")
#os.renames("folder2","test/new_folders")
#os.rmdir("folder")
os.system("")