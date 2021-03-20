def revword(word):
    return word[::-1]

def countword():
    counter = 0
    file = open(r'text.txt')
    index = 0
    for sentence in file:
        if index == 0:
            word = sentence.lower().rstrip()
            index = index +1
            counter = counter + 1
        else:
            sentence = sentence.lower()
            sentence = sentence.split()
            for word1 in sentence:
                word1 = revword(word1)
                if word1 == word:
                    counter = counter + 1
    return counter
print(countword())

