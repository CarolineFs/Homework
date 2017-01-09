#простите за это, но это иногда работает 
import random
k = 0
arrv = ['а', 'о', 'у', 'ы', 'э', 'я', 'ё', 'ю', 'и', 'е'] 
f = open('nounsfemin.txt', 'r', encoding = 'utf - 8')
l = f.readlines()
noun = random.choice(l)
for i in arrv:
    if i in noun:
        k +=1
f2 = open('modiffem.txt', 'r', encoding = 'utf - 8')
l2 = f2.readlines()
modifnoun = random.choice(l2)
for i in arrv:
    if i in modifnoun:
        k +=1
if k == 5:
    str1 = modifnoun + noun
else:
    k = 0
    while k != 5:
        noun = random.choice(l)
        for i in arrv:
            if i in noun:
                k +=1
        modifnoun = random.choice(l2)
        for i in arrv:
            if i in modifnoun:
                k +=1
    str1 = modifnoun + noun
f.close()
f2.close()
k = 0
f3 = open('modverb1.txt', 'r', encoding = 'utf - 8')
l3 = f3.readlines()
modverb1 = random.choice(l3)
for i in arrv:
    if i in modverb1:
        k +=1
f4 = open('modverb2.txt', 'r', encoding = 'utf - 8')
l4 = f4.readlines()
modverb2 = random.choice(l4)
for i in arrv:
    if i in modverb2:
        k +=1
if k == 5:
    str2 = modverb1 + modverb2
else:
    k = 0
    while k != 5:
        modverb1 = random.choice(l3)
        for i in arrv:
            if i in modverb1:
                k +=1
        modverb2 = random.choice(l4)
        for i in arrv:
            if i in modverb2:
                k +=1
    str2 = modverb1 + modverb2
f3.close()
f4.close()
k = 0
f5 = open('verb.txt', 'r', encoding = 'utf - 8')
l5 = f5.readlines()
verb = random.choice(l5)
f5.close()
print (str1)
print (str2)
print (verb)
