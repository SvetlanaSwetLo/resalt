import json
with open("setting.json","r",encoding="utf-8") as file:
# file={"fname": "rrrrrr",
#  "lname": "jjjjjj, ",
# "age": "22"}
    data=json.load(file)# Считать в виде словаря в переменную, теперь дата-словарь
print(data)