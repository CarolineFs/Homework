import os
import re
names = os.listdir()

for i in range (len(names)):
    if os.path.isfile(names[i]) is True:
        index = names[i].rindex('.')
        names[i] = names[i][0:index]
        
def countnum(names):
    k = 0
    flag = 0       
    for i in range (len(names)):
        for j in range (i):
            if names[i] == names [j]:
                flag +=1
                break
        if flag == 0:
            print(names[i])
        flag = 0
        file = re.search('[1-9]', names[i])
        if file != None:
            k += 1
    return k
print ('Всего файлов, в названии которых встретились цифры: ',countnum(names))
