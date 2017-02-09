import re
with open ('Комар обыкновенный — Википедия.html', 'r', encoding = 'utf - 8') as f:
    text = f.read()
result = re.sub ('комар(а(м(ми)?|х)?|у|е|ы|о(в|м))?', 'слон\\1', text, flags = re.U)
result = re.sub ('Комар(а(м(ми)?|х)?|у|е|ы|о(в|м))?', 'Cлон\\1', result, flags = re.U)
with open ('results.html', 'w', encoding = 'utf - 8') as f_res:
    f_res.write(result)
