 
import re 
requests=['+14145898956',
'+14145899499',
'+14148242899',
'+14145893899',
'+12633892299']
specials=['TWLO','CODE','HTCH']
l2n={'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}
# print(l2n)
answer=[]
hot_nums={}
for special in specials:
    num=''
    for letter in special: 
        num+=str(l2n[letter.lower()]) 
    hot_nums[num]=special #creating a dictionary of all numbers that can be mapped to strings
print(hot_nums)
for request in requests:
    for num in hot_nums.keys():
        if re.search( num, request ):  #searching if those numbers exist
            # answer.append(re.sub(num, hot_nums[num], request, flags=re.I)) #replacing the number with a string if it exist
            answer.append(request)
answer.sort
print(answer)
        
            