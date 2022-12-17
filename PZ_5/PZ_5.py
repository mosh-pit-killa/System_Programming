dictionary = {'стул': 'chair', 'стена': 'wall', 'яблоко': 'apple', 'ручка': 'pen', 'дерево': 'tree', 'игра': 'game',
              'мяч': 'ball', 'страна': 'country', 'навык': 'skill', 'огонь': 'fire'}

print('Русско-Английский словарь.')
print('Список доступных для перевода слов: стул, стена, яблоко, ручка, дерево, игра, мяч, страна, навык, огонь.')

while True:
    try:
        word = input('Введите слово на русском языке: ')
        if word == 'завершить' or word == 'quit':
            print('До свидания.')
            break
        print(word + ' - ' + dictionary[word])
        print('RUS' + (' ' * (len(word))) + 'ENG')
        print()
    except KeyError:
        print('Ошибка. Этого слова нет в словаре.')
        print()
