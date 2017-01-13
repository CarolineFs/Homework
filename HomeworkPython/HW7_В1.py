def openfile(name):
    words = []
    with open (name, 'r', encoding = 'utf-8') as f:
        file = f.read()
    file = file.lower()
    words = file.split()
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:')
    return words
def ing_frequency():
    words2 = openfile(name)
    ing_freq = 0
    for i in range(len(words2)):
        if words2[i].endswith('ing'):
            ing_freq += 1
    return ing_freq
def word_freq(word_count_freq):
    words3 = openfile(name)
    w_freq = 0
    for i in range(len(words3)):
        if words3[i] == word_count_freq:
            w_freq += 1
    return w_freq
name = input('File name: ')
word_count_freq = input('Ing - word: ')
word_count_freq = word_count_freq.lower()
ing_frequency()
word_freq(word_count_freq)
print(ing_frequency())
print(word_freq(word_count_freq))
    
