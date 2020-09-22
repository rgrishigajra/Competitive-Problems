
items = [2, 2, 3, 1, 4, 1, 2, 3, 1, 3, 2, 10]
# items = [1, 4, 3, 3, 4, 1, 2, 3, 2, 1, 4, 12]
# items = [1, 1, 1, 4, 1, 3, 1, 1, 3]
import math

def budget_f(pants, shoes, shirts, skirts, budget):
    total=len(pants)+len(shoes)+len(shirts)+len(skirts)
    list_of_items_by_type = [pants, shoes, shirts, skirts]
    for itr in range(len(list_of_items_by_type)):
        list_of_items_by_type[itr].sort()
        min_cost = list_of_items_by_type[itr][0]
        budget -= min_cost
        for product_itr in range(len(list_of_items_by_type[itr])):
            list_of_items_by_type[itr][product_itr] -= min_cost
        list_of_items_by_type[itr] = list_of_items_by_type[itr][1:]
    count = 1
    print(budget, list_of_items_by_type)
    if budget < 0:
        return 0
    for i in range(total):
        temp_budget = budget
        for itr in range(len(list_of_items_by_type)):
            for product_itr in range(len(list_of_items_by_type[itr])):
                if list_of_items_by_type[itr][product_itr] <= temp_budget:
                    count += 1
                    temp_budget -= list_of_items_by_type[itr][product_itr]
                    list_of_items_by_type[itr][product_itr]= math.inf
                    break
    return count


# items = [2,2,3,1,4,1,2,3,1,3,2,10]
len_arr = 0
itr = 0
list_of_items_by_type = []
while itr <= len(items)-2:
    arr = []
    len_arr = items[itr]
    while len_arr > 0:
        itr += 1
        len_arr -= 1
        arr.append(items[itr])
    itr += 1
    list_of_items_by_type.append(arr)
budget = items[itr]
print(budget, list_of_items_by_type)
print(budget_f(list_of_items_by_type[0], list_of_items_by_type[1],
               list_of_items_by_type[2], list_of_items_by_type[3], budget))
print(budget_f([7,8,9,1,6,14],[10,5,7],[5,6,6,4,8,8],[3,12,11,3],30))
def shopping(k,jeans, shoes, skirts, tops):
    dp = [[0]*(k+1) for _ in range(4)]
    res=0
    dictt={1:shoes,2:skirts,3:tops}
    for i in range(len(dp)):
        if i==0:
            for a in range(len(jeans)):
                dp[i][jeans[a]]=1
        else:
            for j in range(len(dp[0])):
                for a in range(len(dictt[i])):
                    if dp[i-1][j]>0 and j+ dictt[i][a]<=k:
                        dp[i][j+dictt[i][a]] += dp[i-1][j]
    for j in range(len(dp[0])):
        res+=dp[3][j]
    return res
print(shopping(budget,[7,8,9,1,6,14],[10,5,7],[5,6,6,4,8,8],[3,12,11,3]))