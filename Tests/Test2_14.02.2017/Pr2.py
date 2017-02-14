import re
with open ('test.html', 'r', encoding = 'utf - 8') as f:
    text = f.readlines()
k = 0
for lines in text:
    if lines == '</teiHeader>\n':
        k += 1
        break
    k += 1;

card = re.compile (r'?type="(.*)?"', flags = re.I|re.DOTALL)
arr_type = []
for lines in text :
    s = str(lines)
    r = re.match(card, s)
    res = r.group(1)
    if res in arr_type:
        break
    arr_type.append(res)
freq = {}
for i in range(len(arr_type)):
    word = arr_type[i]
    try:
        freq[word] += 1
    except:
        freq[word] = 1
print(freq)
