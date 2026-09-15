class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = []
        for n in nums:
            concat.append(n)
        return concat * 2

