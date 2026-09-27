class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # {3:0, 4:1}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[j] = i