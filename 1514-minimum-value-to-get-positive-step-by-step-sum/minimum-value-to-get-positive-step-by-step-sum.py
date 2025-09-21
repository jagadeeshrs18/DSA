class Solution:
    def minStartValue(self, nums):
        running_sum = 0
        min_sum = 0

        # Calculate the running sum and track the minimum sum
        for num in nums:
            running_sum += num
            if running_sum < min_sum:   # Update only when we hit a new low
                min_sum = running_sum

        # Minimum start value to keep total >= 1
        return 1 - min_sum

        