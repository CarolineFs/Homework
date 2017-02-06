import re
with open ('Великобритания — Википедия.html', 'r', encoding = 'utf - 8') as f:
    text = f.read()
card = 'title="Столица(?:.)+\n(?:.)+title="([А-Я][а-я]+)?"'
lines = re.search(card, text)
l = lines.group(1)
with open ('results.txt', 'w', encoding = 'utf - 8') as res:
    res.write(l)
