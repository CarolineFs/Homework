import re
with open ('anna.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    arr =[]
    past = '(открыл(а|и))'
    fut = '(откро(ют?|е(т|шь)))'
    fut2 = '(откро(е(шься|тся)|ются))'
    inf = '(открыть(ся)?)'
    part_m = '(открыт(ы(ый|тому|тым)|о(м|го)))'
    part_fem = '(открыт(ая|ой|ую))'
    part_n = '(открытое)'
    part_plur = '(открыты(е|ых|ыми?))'
    part_short = '(открыт(а|ы)?)'
    part2 = '(открыв)'
    smth = '(будучи открыт(ыми?|ой))'
    part3_m = '(открывш(ий|его|ему|ем))'
    part3_n = '(открывшее)'
    part3_fem = '(открывш(ая|ей|ею))'
    part3_plur = '(открывши(е|х|м))'
    ind = '(открой(те)?)'
    for word in words:
        p = re.search(past, word)
        if p != None:
            if word not in arr:
                arr.append(word)
        f = re.search(fut, word)
        if f != None:
            if word not in arr:
                arr.append(word)
        f2 = re.search(fut2, word)
        if f2 != None:
            if word not in arr:
                arr.append(word)
        i = re.search(inf, word)
        if i != None:
            if word not in arr:
                arr.append(word)
        p_m = re.search(part_m, word)
        if p_m != None:
            if word not in arr:
                arr.append(word)
        p_f = re.search(part_fem, word)
        if p_f != None:
            if word not in arr:
                arr.append(word)
        p_n = re.search(part_n, word)
        if p_n != None:
            if word not in arr:
                arr.append(word)
        p_p = re.search(part_plur, word)
        if p_p != None:
            if word not in arr:
                arr.append(word)
        p_s = re.search(part_short, word)
        if p_s != None:
            if word not in arr:
                arr.append(word)
        p2 = re.search(part2, word)
        if p2 != None:
            if word not in arr:
                arr.append(word)
        sm = re.search(smth, word)
        if sm != None:
            if word not in arr:
                arr.append(word)
        p3_n = re.search(part3_n, word)
        if p3_n != None:
            if word not in arr:
                arr.append(word)
        p3_m = re.search(part3_m, word)
        if p3_m != None:
            if word not in arr:
                arr.append(word)
        p3_f = re.search(part3_fem, word)
        if p3_f != None:
            if word not in arr:
                arr.append(word)
        p3_p = re.search(part3_plur, word)
        if p3_p != None:
            if word not in arr:
                arr.append(word)
        indic = re.search(ind, word)
        if indic != None:
            if word not in arr:
                arr.append(word)
               
print(arr)

