string="yeah this is a csv,'test','is it, yeah!'"
result=['START']
single_quote=False
sentence=""
for itr,char in enumerate(string):
    if char == "'" :
        single_quote = not single_quote
        continue
    if char == "," and not single_quote:
        result.append(sentence)
        sentence = ''
        continue
    sentence+=char
result.append(sentence)
result.append('END')
print(result)
# ['yeah this is a csv', 'test', 'is it, yeah!']