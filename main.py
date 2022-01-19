with open("input1.txt","r",encoding="utf-8") as file:
    students=[]
    for i in file:
        students.append(i.strip().split())
print(students)
s=0
bad_students=[]
for student in students:
    s+=int(student[2])
    if int(student[2])<3:
        bad_students.append(student[0])
with open("output11.txt","w",encoding="utf-8") as file:
    file.write(f"Средний балл по классу - {s / len(students)}, Учащиеся, чья оценка меньше 3 - {','.join(bad_students)}")
