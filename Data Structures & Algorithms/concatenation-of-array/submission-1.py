class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #initialize empty list
        concat = []
        #store all nums in list 
        for n in nums:
            concat.append(n)
        #return list repeated x2 
        return concat * 2

