# -*- coding: utf-8 -*-

name = str("Имя:" + input('Введите имя: '))
family = str("Фамилия:" + input('Введите фамилию: '))
age = str("Возраст:" + input('Введите возраст: '))
city = str('Город:' + input('Введите город: '))

I = [name, family, age, city]
f = open("Result.txt", "w", encoding="utf-8")

for item in I:
        f.write("%s\xa0" % item)

f.write('\n')
f.close()
f = open("Result.txt", "r", encoding="utf-8")
k = f.read()

print(k)