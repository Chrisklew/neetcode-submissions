class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize empty set to store unique Nums
        uniqueNums = set()
        #iterate through each value in list nums
        for n in nums:
            #return true if duplicate shows
            if n in uniqueNums:
                return True
            #otherwise add n value into set
            uniqueNums.add(n)
        #if duplicate value not found return False
        return False