# 
o=''
i="DLDD"
s='LDWDL'

def rearrange(s,o):
    for i in range(len(s)):
        if s[i]=='W':
            o+='W'
            s=s[:i]+s[i+1:]
            break
    for i in range(len(s)):
        if s[i]=='D':
            o+='D'
            s=s[:i]+s[i+1:]
            break
    for i in range(len(s)):
        if s[i]=='L':
            o+='L'
            s=s[:i]+s[i+1:]
            break
    if len(s)!=0:
        o = rearrange(s,o)
    return o

print(rearrange(i,o))
print(rearrange(s,o))
