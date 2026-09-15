class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums: 
            #get count of each number of times number appears
            count[n] = 1 + count.get(n, 0)
        
        #this will return every kv pair we added to our dictionary
        for n, c in count.items():
            #this value n is occuring c number of times
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                