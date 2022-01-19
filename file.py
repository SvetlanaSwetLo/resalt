lst=[]
with open ("input.txt","r", encoding="utf-8") as file: #считываем построчно
    lst=[i.strip() for i in file]
print(lst)
result=[]
for i,j in enumerate(lst):
    count_word=j.count(" ")+1
    count_letter =0
    for k in j:
        if k.isalpha():
            count_letter+=1
    text=f"В {i+1} строке: {count_word} слов, {count_letter} букв"
    result.append(text)
with open("output.txt", "w",encoding="utf-8") as file:
    file.write("\n".join(result))