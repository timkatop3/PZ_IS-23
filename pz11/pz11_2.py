# Из предложенного текстового файла (text18-23.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.

al = open('pz11/text18-23.txt', 'r', encoding='utf-16')

content = al.readlines()


for line_n, line in enumerate(content):
    print(line)

cont = content[:4]
punctuation = 0
for i in cont:
    for y in i:
        if y in ",.:;?!":
            punctuation +=1
print('В первых четырех строках ',punctuation ,'знака пунктуации')

ne = open('pz11/stix.txt', 'w', encoding='utf-16')

for y in content:
    form_al = y.lower()
    ne.write(form_al)