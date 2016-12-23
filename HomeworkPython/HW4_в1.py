word=input('Введите слово: ')
s = len(word)
print (word)
while s != 0:
    s = s - 1
    word = word [0:s]
    print (word)
