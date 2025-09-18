class Solution:
    def subarraysWithKDistinct(self, nums, k):
        # Helper function: counts subarrays with at most k distinct numbers
        def atMost(k):
            count = {}
            left = 0
            res = 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                # If more than k distinct, shrink window
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                # Add number of subarrays ending at right
                res += (right - left + 1)
            return res

        # Exactly k distinct = atMost(k) - atMost(k - 1)
        return atMost(k) - atMost(k - 1)



        