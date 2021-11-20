FILE_NAME = "words.txt"
words_writer = None
words_reader = None
try:
    words_writer = open(FILE_NAME, "w")
    words_writer.write("ilya")
except FileNotFoundError as fe:
    print(fe)
finally:
    words_writer.close()


try:
    words_reader = open(FILE_NAME, "r")
    words_content = words_reader.read()
    print(words_content)
except FileNotFoundError as fe:
    print(fe)
finally:
    words_reader.close()

