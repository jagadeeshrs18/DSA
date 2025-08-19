class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0   # total subarrays
        length = 0  # length of current zero block

        for num in nums:
            if num == 0:
                length += 1
                count += length   # add all subarrays ending at this index
            else:
                length = 0   # reset when non-zero found

        return count