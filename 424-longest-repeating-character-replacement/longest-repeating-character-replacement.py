class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency array for uppercase characters 'A'-'Z'
        freq = [0] * 26
        
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # 1. Update frequency of current character
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            # 2. Track the most frequent character count in current window
            max_freq = max(max_freq, freq[index])

            # 3. If replacements needed > k, shrink window from the left
            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            # 4. Update the maximum valid window length
            max_length = max(max_length, right - left + 1)

        return max_length




 