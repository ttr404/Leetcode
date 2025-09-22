class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  # number → index
        for i, num in enumerate(nums):
            dif = target - num
            if dif in hashmap:
                return [hashmap[dif], i]
            hashmap[num] = i
        return []

nums = [0,2,7,8]
target = 9
print(Solution().twoSum(nums, target))



