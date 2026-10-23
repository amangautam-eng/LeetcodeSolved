class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num==0 or num==1:
            return True

        left,right=1,num//2

        while left<=right:

            mid= left + (right-left)//2

            if mid*mid == num:
                return True
            elif mid*mid > num:
                right=mid-1
            else:
                left=mid+1

        return False
        