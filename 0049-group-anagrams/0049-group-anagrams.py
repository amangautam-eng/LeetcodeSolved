class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq={}
        ans=[]
        for char in strs:
            sorted_char=str(sorted(char))

            if sorted_char in freq:
                freq[sorted_char].append(char)

            else:
                freq[sorted_char]=[char]

        for x in freq:
            ans.append(freq[x])

        return ans

        
        