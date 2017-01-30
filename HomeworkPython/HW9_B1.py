import re
with open ('anna.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    arr =[]
    past = 'открыл(а|и)'
    fut = 'откро(ют?|е(т|шь)|е(шься|тся)|ются|й(те)?)'
    part = 'открыт(ы(ый|тому|тым)|о(м|го)|ая|ой|ую|а|ы|ые|ых|ыми?|ое)'
    smth = 'будучи открыт(ыми?|ой)'
    inf = 'откры(в(ш(ий|его|ему|ем|ее|ая|ей|ею|ие|их|им))?|ть(ся)?)'

    for word in words:
        p = re.search(past, word)
        if p != None:
            if word not in arr:
                arr.append(word)
        f = re.search(fut, word)
        if f != None:
            if word not in arr:
                arr.append(word)
        i = re.search(inf, word)
        if i != None:
            if word not in arr:
                arr.append(word)
        p_m = re.search(part, word)
        if p_m != None:
            if word not in arr:
                arr.append(word)
        sm = re.search(smth, word)
        if sm != None:
            if word not in arr:
                arr.append(word)
                              
print(arr)



