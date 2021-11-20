FILE_NAME = "hebrew_file.txt"

hebrew_letters = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר",
                  "ש", "ת"]
lines_to_write = list()
lines_read = str()

for number_symbol, hebrew_letter in enumerate(hebrew_letters, 1):
    lines_to_write.append('%s-%d\n' % (hebrew_letter, number_symbol))

with open(FILE_NAME, "w", encoding='utf-8') as hebrew_file:
    hebrew_file.writelines(lines_to_write)

with open(FILE_NAME, "r", encoding='utf-8') as hebrew_file:
    chunk_size = 8
    hebrew_content = str()

    chunk = hebrew_file.read(chunk_size)
    hebrew_content += chunk
    while chunk:
        chunk = hebrew_file.read(chunk_size)
        hebrew_content += chunk
    lines_read = hebrew_content.splitlines(keepends=True)

if not(lines_read == lines_to_write):
    print("Read different content from that was written")
print("".join(lines_read))


