class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        largest_cap = 0
        while i < j:
            amt = min(height[i],height[j]) * (j - i)
            if amt > largest_cap:
                largest_cap = amt
            
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                if height[i+1] >= height[j-1]:
                    i += 1
                elif height[i+1] < height[j-1]:
                    j -= 1
        return largest_cap

        
        