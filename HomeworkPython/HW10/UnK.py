import re
with open ('Великобритания — Википедия.html', 'r', encoding = 'utf - 8') as f:
    text = f.read()
card = '<tr>\n<td>(?:.)+title="Столица(?:.)+\n(?:.)+title="(.*)"'
lines = re.search(card, text)
l = lines.group(1)
with open ('results.txt', 'w', encoding = 'utf - 8') as res:
    res.write(l)