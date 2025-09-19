# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def pivotIndex(self, nums):
        # Step 1: Initialize leftSum and rightSum
        leftSum, rightSum = 0, sum(nums)  # rightSum is initially total sum of array

        # Step 2: Loop through each index and value
        for idx, ele in enumerate(nums):
            # Step 3: Before checking, remove current element from rightSum
            rightSum -= ele

            # Step 4: Check pivot condition
            if leftSum == rightSum:
                return idx  # Found the pivot index

            # Step 5: Add current element to leftSum for next iteration
            leftSum += ele

        # Step 6: If no pivot index found, return -1
        return -1
   




      


        