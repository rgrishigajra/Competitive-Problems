class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=='' or len(s)<len(t) or t=='':
            return ""
        start = 0
        result = 0
        min_len = math.inf
        pat = collections.defaultdict(int)
        for char in t:
            pat[char]+=1
        matched = 0
        for end,char in enumerate(s):
            if char in pat:
                pat[char]-=1
                if pat[char]>=0:
                    matched+=1
            while matched == len(t):
                if min_len > end-start+1:
                    min_len = end-start+1
                    result = start
                left_char = s[start]
                if left_char in pat:
                    if pat[left_char] == 0:
                        matched-=1
                    pat[left_char]+=1
                start+=1
        return s[result:result+min_len] if min_len<=len(s) else ''
                    
                    