# word_source1 = ["the", "bats", "act", "tabs", "cat", "in" ]
# sentences1= ['cat the bats', 'in the act', 'act tabs in']
# word_source2=['star',
# 'tars',
# 'stay',
# 'tay',
# 'seed',
# 'dees',
# 'eesd',
# 'rast',
# 'date',
# 'ate']
# sentencea2= [
# 'ate date stay',
# 'rast tay star',
# 'tay stay tars',
# 'seed dees star',
# 'ate seed rast'
# ]
word_source3=[
'date',
'tead',
'seed',
'dees',
'west',
'stew',
'tado',
'toad',
'said',
'aids',
'in',
'the',
'bate',
'tabe',
'coast',
]
sentences3=[
    'date seed west',
'stew the in',
'coast in west',
'dees west bate',
'said date tead',
]
import math
from collections import defaultdict

def get_anagrams(source):
    d = defaultdict(list)
    s= {}
    for word in source:
        if len(word) >1:
            key = "".join(sorted(word))
            d[key].append(word)
            s[word]=key
    return [d,s]

[d,s] = get_anagrams(word_source2)
# print(d,s)
results=[]
for sentence in sentences2:
    count=1
    for word in sentence.split(' '):
        if word in s:
            if len(d[s[word]])>1:
                count=count*math.comb(len(d[s[word]]),1)    
    results.append(count)
print(results)
    



