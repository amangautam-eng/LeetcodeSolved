class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        decrypted =[0]*n

        if k==0:
            return decrypted
    
        if k > 0:
            start, end = 1, k
        else:
            start, end = n + k, n - 1
            
        current_window_sum = 0
        for i in range(start, end + 1):
            current_window_sum += code[i % n]
        decrypted[0] = current_window_sum
        
        for i in range(1, n):
            current_window_sum -= code[start % n]
            start += 1
            end += 1
            current_window_sum += code[end % n]
            decrypted[i] = current_window_sum
            
        return decrypted