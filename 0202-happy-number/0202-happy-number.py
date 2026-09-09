class Solution:
    def isHappy(self, n: int) -> bool:

        def sqr(x):
            s=0
            while x:
                dig=x%10
                x=x//10
                s+=dig**2
            return s

        def check(x,y):
            if x==y and x==1:
                return True
            if x==y and x!=1:
                return False

            return check(sqr(x),sqr(sqr(y)))

        return check(sqr(n),sqr(sqr(n)))

        