text=input('Введите текст: ').lower()
text1=text.replace(' ','')
vowels='уеыаоэяию'
vowels_count=0
consonants_count=0
for i in text1:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
print("Гласных букв", vowels_count)
print("Соглысных букв",consonants_count)
for i in text1:
    if vowels_count==consonants_count and i in vowels:
        print(i, end=' ')

