class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for idx, num in enumerate(nums):
            l = []
            di = num >= 0
            slow = fast = idx
            while True:
                slow = (slow + nums[slow]) % len(nums)
                temp = (fast + nums[fast]) % len(nums)
                fast = (temp + nums[temp]) % len(nums)
                # checking for 1 length cycle and check if already visited
                if (fast == temp) or fast in visited or temp in visited:
                    break
                # check for positive directions
                if di and (nums[slow] < 0 or nums[fast] < 0 or nums[temp] < 0):
                    break
                # check for negative directions
                if not di and (nums[slow] > 0 or nums[fast] > 0 or nums[temp] > 0):
                    break
                if slow == fast:
                    return True
                l.append(slow)
                l.append(fast)
            visited.update(l)
        return False
