class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = collections.defaultdict(list)
        for word in strs:
            key = [0 for _ in range(26)]
            for char in word:
                key[ord(char)-ord('a')]+=1
            freq[tuple(key)].append(word)
        return [freq[k] for k in freq.keys()]