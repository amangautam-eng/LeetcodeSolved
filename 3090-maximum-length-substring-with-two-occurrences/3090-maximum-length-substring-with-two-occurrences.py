class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        cnt ={}

        for right in range(0,len(s)):
            char=s[right]

            cnt[char] = cnt.get(char,0) + 1

            while cnt[char]>2:
                lchar=s[left]

                cnt[lchar]-=1
                left+=1

            maxlen= max(maxlen, right-left+1)

        return maxlen

        