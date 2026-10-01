class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        valid ={')':'(','}':'{',']':'['}

        for char in s:
            if char in valid:
                curr=stack.pop() if stack else "#"

                if curr!=valid[char]:
                    return False
            else:
                stack.append(char)

        return len(stack)==0