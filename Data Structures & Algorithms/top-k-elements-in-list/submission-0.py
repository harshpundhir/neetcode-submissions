class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {} # or I could have done it using defalut dict
        for i in nums:
            hmap[i] =  hmap.get(i,0) + 1
        
        freq = []
        for key,v in hmap.items():
            freq.append(v)
        
        freq = sorted(freq, reverse=True)
        print(freq)


        ans = [key for key,val in hmap.items() if val in freq[:k] ]
        return ans
            

        


     


        