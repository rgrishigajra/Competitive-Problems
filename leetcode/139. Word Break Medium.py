class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([0])
        mini = math.inf
        dic = set()
        dic = set(wordDict)
        visited = set()
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in dic:
                    if end == len(s):
                        return True
                    q.append(end)
                visited.add(start)
        return False
