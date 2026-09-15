class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashmap to store key value pairs 
        prevMap = {} #val: index

        #enumerate takes iteratable and returns pairs 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
            