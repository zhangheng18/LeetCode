import random


class RandomizedSet:
    def __init__(self):
        self.val2idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val2idx:
            return False
        self.val2idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val2idx:
            return False
        # 元素和最后一个元素交换
        val_idx = self.val2idx[val]
        self.val2idx[self.nums[-1]] = val_idx
        self.nums[val_idx], self.nums[-1] = self.nums[-1], self.nums[val_idx]
        # 删除val
        self.nums.pop()
        del self.val2idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
