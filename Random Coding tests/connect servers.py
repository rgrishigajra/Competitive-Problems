class UnionFind:
    def __init__(self, n, connections):
        self.servers = set()
        for a, b, c in connections:
            self.servers.add(a)
            self.servers.add(b)
        self.parents = {x: x for x in self.servers}
        self.ranks = {x: 1 for x in self.servers}

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False
        if self.ranks[p2] > self.ranks[p2]:
            p1, p2 = p2, p1
        self.parents[p2] = p1
        self.ranks[p1] += self.ranks[p2]
        return True


def minimumCostConnections(num, connections):
    arr = []
    l = {}
    cities = set()
    for con in connections:
        cities.add(con.firstTown)
        cities.add(con.secondTown)
        arr.appned([con.firstTown, con.secondTown, con.cost])
        l[con.firstTown+con.secondTown+str(con.cost)] = con
    arr.sort(key=lambda x: x[2])
    uf = UnionFind(num, arr)
    min_cost = 0
    result = []
    for serv1, serv2, cost in arr:
        if uf.union(serv1, serv2):
            result.append(l[serv1+con.serv2+str(cost)])
    return result if len(result) == len(cities)-1 else []
