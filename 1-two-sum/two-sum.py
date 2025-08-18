class Solution:
  def twoSum(self, nums, target):
        # Create an empty hashmap (dict) to store number -> index
        hashmap = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            # Find the number needed to reach target
            complement = target - num
            
            # If we have seen the complement before, return the indices
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # Otherwise, store this number and its index
            hashmap[num] = i
