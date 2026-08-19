class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        store=[[] for _ in range(len(nums)+1)]
        res=[]

        for num in nums:
            freq[num] = 1 +freq.get(num,0)

        for num,v in freq.items():
            store[v].append(num)

        ptr=len(store)-1
        
        while len(res)<k:
            for x in store[ptr]:
                res.append(x)
                if len(res)==k:
                    break

            ptr-=1

        return res

        
        