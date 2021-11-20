FILE_NAME = "words.txt"

with open(FILE_NAME, "w") as words_writer:
    words_writer.write("ilya")

with open(FILE_NAME, "r") as words_reader:
    print("\n".join(words_reader.readlines()))

