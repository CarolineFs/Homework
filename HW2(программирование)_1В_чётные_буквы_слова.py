w = input('Введите слово (в кириллице): ')
wl=w.lower()
a='а'
k='к'
if a in wl:
    wl=wl.replace('а',' ')
if  k in wl:
    wl=wl.replace('к', ' ')
r=wl[1: : 2]
r=r.replace(' ','')
print ('Чётные буквы введенного слова, кроме "а" и "к":',r)

