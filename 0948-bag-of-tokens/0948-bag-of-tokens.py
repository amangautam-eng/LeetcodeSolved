class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:

        sort=sorted(tokens)
        left,right=0,len(sort)-1
        score,max_score=0,0

        while left<=right:
            if power>=sort[left]:
                power-=sort[left]
                score+=1
                left+=1
                max_score=max(score,max_score)

            elif score>0 and left<right:
                power+=sort[right]
                score-=1
                right-=1
            
            else:
                break

        return score
        