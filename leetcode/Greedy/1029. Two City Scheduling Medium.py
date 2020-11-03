class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        total = 0
        n = len(costs)//2
        for itr in range(n):
            total += costs[itr][0] + costs[itr+n][1]
        return total
    