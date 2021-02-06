from collections import defaultdict
from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_map = defaultdict(int)
        self.values_array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index_map:
            return False
        self.values_array.append(val)
        self.index_map[val] = len(self.values_array)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index_map:
            return False
        delete_index = self.index_map[val]
        self.index_map[self.values_array[-1]] = delete_index
        self.values_array[delete_index] = self.values_array[-1]
        self.values_array.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.values_array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
