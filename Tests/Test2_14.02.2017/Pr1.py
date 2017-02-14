with open ('test.html', 'r', encoding = 'utf - 8') as f:
    text = f.readlines()
k = 0
for lines in text:
    if lines == '</teiHeader>\n':
        k += 1
        break
    k += 1;
        
k = str(k)
with open ('result.txt', 'w', encoding = 'utf - 8') as f_result:
    f_result.write(k)
