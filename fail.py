with open ("input8.txt","r", encoding="utf-8") as file: #считываем построчно
        lst=[i.strip() for i in file]
        lst1="\n".join(lst)
print(lst1)
print(type(lst1))
lst2=lst1.split(" ")
print(lst2)
vowels="eyuioaуеыаоэяию"
vowels_words=0
consonants_words=0
for i in lst2:
    if i[0].lower() in vowels:
        vowels_words+=1
    else:
         consonants_words+=1
print(vowels_words)
print(consonants_words)
if vowels_words>consonants_words:
        print("больше слов на гласную букву")
else:
        print("больше слов на согласную букву")
with open("output8.txt","w", encoding="utf-8") as file:
     file.write(lst1)

