from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        # Edge case: If nums is empty or k is zero
        if not nums or k == 0:
            return []
        
        dq = deque()  # Deque to store indices
        result = []   # To store the max for each window

        # Iterate through each element in nums
        for i in range(len(nums)):
            # Step 1: Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Step 2: Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Step 3: Add current index
            dq.append(i)

            # Step 4: Start adding results once we have the first valid window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
 

             
            



        