class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initialize list
        temp = []
        #iterate through list to find existing nums that equal val
        for n in nums:
            if n == val:
                continue
            temp.append(n)

        #iterate through loop
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return len(temp)


        