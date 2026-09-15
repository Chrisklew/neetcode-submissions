class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize dictionary 
        prevMap = {}
        #iteration 1  0 , 3 -->  difference = 7 - 3 = 4 , prevMap = {3:0}
        #iteration 2  1 , 4 --> difference = 7-4= 3, prevMap = {3:0, 4:1}
        for i, j in enumerate(nums):
            difference = target - j
            #it2. since difference = 3 is stored in prevMap = {3:0}
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[j] = i
