class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        digit=""
        ans=[]
        
        for x in digits:
            digit+=str(x)

        digit=int(digit)+1

        for c in str(digit):
            ans.append(int(c))

        return ans