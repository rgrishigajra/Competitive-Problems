def countStrings(s):
    n = len(s)   
    temp = s + s 
    count=0
    for i in range(n) :  
        if temp[i] ==temp[n+i-1]:
            count+=1
    return count