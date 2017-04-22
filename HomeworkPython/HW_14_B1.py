import os
maximum = 0
for roots, dirs, files in os.walk('.'):
    s = str(roots)
    s = s.replace('/', '\\')
    a = []
    a = s.split('\\')
    if len(a)>maximum:
        maximum = len(a)
print(maximum-1)
