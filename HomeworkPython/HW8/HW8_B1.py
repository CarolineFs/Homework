#программа загадывает слова. 
#Пользователю даётся столько попыток угадать слово, сколько букв в слове.
import csv
import random
clues = {}
f = open('clues.csv', 'r', encoding='utf-8') 
text = csv.reader(f, delimiter=';')
for word in text:
    clues[word[0]] = word[1]
values = list(clues.values())
keys = list(clues.keys())
n = random.choice([0, 1,2,3,4,5,6,7,8,9,10])
l = len (values[n])
k = 0
i = 1
while i <= l:
    response = input (keys[n]+' '+'...'+' ')
    k += 1
    i += 1
    if response == values [n]:
        print('Вы победили!')
        break
    else:
        print ('Нет!')
if response != values[n]:
    print('Вы проиграли!')
