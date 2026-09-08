class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ran,freq_mag={},{}

        for c in ransomNote:
            freq_ran[c]=1+freq_ran.get(c,0)
        for c in magazine:
            freq_mag[c]=1+freq_mag.get(c,0)

        for c in ransomNote:
            if c in freq_mag and freq_ran[c]<=freq_mag[c]:
                continue
            else:
                return False

            
            

        return True
        

        