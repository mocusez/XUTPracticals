string = input("Text: ")
words = [word for word in string.split()]

word_count = {}
for word in words:
    previous_count = word_count.get(word, 0)
    word_count[word] = previous_count + 1

for i in sorted(word_count):
    print("{:{}} : {}".format(i, len(word_count), word_count[i]))
