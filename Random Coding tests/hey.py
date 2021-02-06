def social_graphs(counts):
    groups = []
    dic = {}
    for i in range(len(counts)):
        if counts[i] not in dic:
            if counts[i]!=1:
                dic[counts[i]]=[1,len(groups)]
            groups.append([i])
        else:
            group_num = dic[counts[i]][1]
            group_count = dic[counts[i]][0]
            groups[group_num].append(i)
            if group_count+1==counts[i]:
                del dic[counts[i]]
            else:
                dic[counts[i]]=[group_count+1,group_num]
    print(groups)
    groups.sort()
    for group in groups:
        s = ''
        for person in group:
            s+=str(person)+' '
        print(s)

social_graphs([3,3,3,3,1,3])
        
