file=open("../ee.txt","r", encoding="utf-8")
lst=[]
for i in file:
    lst.append(i.strip())
print(lst)
    #lst=[i.strip() for i in file]
with open("../ee.txt","a", encoding="utf-8") as file:
    file.write("\n finish")