class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #key value pair
        #enumerate function takes an iterable and returns pairs (index element)
        #index(i) is the starting value in list Nums we work with. if n 
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                #return pair of indices of index
                return[prevMap[diff], i]
            #if it doesnt exist add to the dict
            prevMap[n] = i
        return