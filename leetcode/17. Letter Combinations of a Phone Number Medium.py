class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combinations = deque([''])
        for digit in digits:
            for _ in range(len(combinations)):
                c = combinations.popleft()
                for letter in phone[digit]:
                    combinations.append(c+letter)
        return combinations
