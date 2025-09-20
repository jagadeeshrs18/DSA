class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        
        for i, x in enumerate(arr):
            total = (i + 1) * (n - i)
            odd = (total + 1) // 2
            ans += x * odd
            
        return ans


             
          
            

               

            


        