FILE_NAME = "hebrew_file.txt"

hebrew_letters = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר",
                  "ש", "ת"]
lines = list()
for number_symbol, hebrew_letter in enumerate(hebrew_letters, 1):
    lines.append('%s-%d\n' % (hebrew_letter, number_symbol))

with open(FILE_NAME, "w", encoding='utf-8') as hebrew_file:
    hebrew_file.writelines(lines)

with open(FILE_NAME, "r", encoding='utf-8') as hebrew_file:
    for line in hebrew_file:
        print(line, end='')
