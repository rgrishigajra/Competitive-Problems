from collections import defaultdict
import re


def isKangaroo(a, b):
    if len(b) == 0:
        return True
    if len(a) == 0:
        return False
    charIndex = defaultdict(int)
    pos = 0
    prev_char = 0
    for index, char in enumerate(a):
        if char == prev_char:
            charIndex[prev_char] = index
        if char == b[pos]:
            charIndex[b[pos]] = index
            prev_char = char
            pos = min(pos+1, len(b)-1)
    if pos != len(b)-1:
        return False
    prev_index = charIndex[b[0]]
    cont_flag = True
    for char in b[1:]:
        if char not in charIndex:
            return False
        if charIndex[char] != prev_index+1:
            cont_flag = False
        prev_index = charIndex[char]
    return not cont_flag
# print(isKangaroo('cantainer','can'))
# print(isKangaroo('devil','evil'))
# print(isKangaroo('devilishly','evil'))
# print(isKangaroo('lighted','lit'))
print(isKangaroo('illuminated','lit'))


def kangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    score = 0
    word_map = defaultdict(int)
    kangaroo_words = defaultdict(int)
    for word in words:
        word_map[word.lower()] += 1
    for row in wordsToSynonyms:
        row = row.lower()
        word, *synonyms = re.split(':|,', row)
        if word not in word_map:
            continue
        for synonym in synonyms:
            check = isKangaroo(word, synonym)
            if check:
                score += 1
                kangaroo_words[synonym] += 1
    for row in wordsToAntonyms:
        row = row.lower()
        word, *antonyms = re.split(':|,', row)
        if word not in word_map:
            continue
        for antonym in antonyms:
            check = isKangaroo(word, antonym)
            if check:
                score -= 1
                kangaroo_words[antonym] += 1
    for word in kangaroo_words:
        if kangaroo_words[word] > 1:
            score += kangaroo_words[word]*(kangaroo_words[word]-1)/2
    return score


words = ['illuminated', 'animosity', 'deoxyribonucleic',
         'container', 'lit', 'amity', 'encourage', 'lighted']
wordsToSynonyms = ['encourage:urge,boost,empire',
                   'container:tin,can,bag,bottle', 'lighted:lit', 'illuminated:lit']
wordsToAntonyms = ['encourage:discourage',
                   'animosity:amity,like', 'lighted:dark']
print(kangarooScore(words, wordsToSynonyms, wordsToAntonyms))
