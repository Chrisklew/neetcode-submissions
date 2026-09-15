class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # 1st iteration: 0, 3 --> diff = 4 , prevMap = {3 : 0}
        # 2nd iteration: 1, 4 --> diff = 3 , prevMap = {3 : 0} 
        # prevMap[3] = 0 and i = 1 , therefore return [0 , 1]
        for i, j in enumerate(nums):
            difference = target - j
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[j] = i
            