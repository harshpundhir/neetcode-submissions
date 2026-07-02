class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for i in strs:
            sorted_strs.append("".join(sorted(i)))
        
        sorted_strs = set(sorted_strs)
        sorted_strs = list(sorted_strs)
        
        

        ans = []
        for i in sorted_strs:
            temp = []
            for j in strs:
                if i=="".join(sorted(j)):
                    temp.append(j)
            ans.append(temp)

        return ans
                




        