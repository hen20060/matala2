def revword(word):
    return word[::-1].lower

def countword():
    counter = 0
    file = open('text.txt')
    word = file[0].lower()
    for sentence in file:
        if sentence != file[0]:
            sentence=sentence.split()
            for word1 in sentence:
                word1 = revword().lower()
                if word1 == word:
                    counter = counter + 1
    return counter
print(countword())
