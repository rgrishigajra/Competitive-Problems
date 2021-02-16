class Record:
    def __init__(self, username, timestamp, website):
        self.name = username
        self.time = timestamp
        self.site = website

    def __repr__(self):
        return f'{self.name} {self.site} {self.time}'


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        records = []
        for idx in range(len(username)):
            records.append(
                (Record(username[idx], timestamp[idx], website[idx])))
        records.sort(key=lambda x: x.time)
        # print(records)
        seq3 = collections.defaultdict(int)
        users = collections.defaultdict(list)
        for record in records:
            users[record.name].append(record.site)
        for user, sites in users.items():
            combos = set(itertools.combinations(sites, r=3))
            for combo in combos:
                seq3[combo] += 1
        max_visit = 0
        max_seq = ''
        for seq, freq in seq3.items():
            if (max_visit < freq) or (max_visit == freq and max_seq > seq):
                max_seq = seq
                max_visit = freq
        return list(max_seq)
