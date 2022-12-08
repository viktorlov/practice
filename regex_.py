import re

txt = "Три богатыря", "проверка", 'Ура'

for x in txt:
    c = re.findall(r"(^[а-я]*[А-Я][а-я]*)$", x)
    print(c)
