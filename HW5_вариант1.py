lines = 0 
flag = 0
words = 0
with  open ('file.txt', 'r', encoding = 'utf - 8') as f:
    for line in f:
        lines+=1
        for letter in line:
            if letter != ' ' and flag ==0:
                words+=1
                flag = 1
            elif letter == ' ':
                flag = 0
av=words/lines
av = round(av, 4)
f.close()
print (av)
