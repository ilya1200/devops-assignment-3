FILE_NAME = "words.txt"
words_writer = None

try:
    words_writer = open(FILE_NAME, "w")
    words_writer.write("ilya")
except FileNotFoundError as fe:
    print(fe)
finally:
    words_writer.close()


with open(FILE_NAME, "r") as words_reader:
    words_content = words_reader.read()
    print(words_content)

