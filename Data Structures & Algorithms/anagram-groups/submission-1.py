class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in result:
                result[x].append(strs[i])
            
            else:
                result[x] = [strs[i]]
        
        return list(result.values())

            
