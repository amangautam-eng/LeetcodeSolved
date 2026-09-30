class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow/edge case for 32-bit signed integers
        # MAX_INT = 2147483647, MIN_INT = -2147483648
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            # Shift left (multiply by 2) as long as it doesn't exceed the dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient