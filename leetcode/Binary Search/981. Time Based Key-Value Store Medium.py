
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_store = collections.defaultdict(
            list)  # each key will be equal to a time sorted list of lists[time,value]
        self.time_stamp = 0
        self.value = 1

    # returns a string such that time_stamp <= key
    def binary_search_val(self, key, arr):
        l, h = 0, len(arr)-1
        if key < arr[l][self.time_stamp]:
            return ""
        while l <= h:
            mid = (l+h)//2
            if arr[mid][self.time_stamp] == key:
                return arr[mid][self.value]
            if arr[mid][self.time_stamp] < key:
                l = mid + 1
            else:
                h = mid - 1
        return arr[h][self.value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append([timestamp, value])
        return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_store:
            return self.binary_search_val(timestamp, self.key_store[key])
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
