w = input('Введите слово (в кириллице): ')
wl=w.lower()
a='а'
k='к'
for a in wl:
    wlra=wl.replace('а',' ')
for k in wlra:
    wlrak=wlra.replace('к', ' ')
r=wlrak[1: : 2]
rs=r.replace(' ','')
print ('Чётные буквы введенного слова, кроме "а" и "к":',r)
