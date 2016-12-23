w = input('Введите слово (в кириллице): ')
w=w.lower()
a='а'
k='к'
if a in w:
    w=w.replace('а',' ')
if  k in w:
    w=w.replace('к', ' ')
w=w[1: : 2]
w=w.replace(' ','')
print ('Чётные буквы введенного слова, кроме "а" и "к":',w)



