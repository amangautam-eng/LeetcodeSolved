class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add current fruit to the basket
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            # Shrink window if we have more than 2 types of fruit
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
                
            # Calculate the maximum consecutive fruits collected
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits
