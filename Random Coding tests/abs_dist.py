from collections import defaultdict
def distance_matrix(arr):
    d = defaultdict(list)
    for i,a in enumerate(arr):
        d[a] += [i]
    print(d)
    dm = [0 for i in range(len(arr))]
    print(dm)
    for i in d.keys():
        for index,k in enumerate(d[i]):
            j=index+1
            while j < len(d[i]):
                print(d[i][j],k,d[i])
                test=abs(d[i][j]-k)
                dm[k]+=test
                dm[d[i][j]]+=test
                j+=1
    print(dm)
    return dm

nums = [1,2,1,1,2,3]
# nums = [1,2,2,1,5,1]

# [] 

distance_matrix(nums)