class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26  # Fixed array for 'A'-'Z'
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Current character index
            idx = ord(s[right]) - 65  # 65 = ord('A')
            freq[idx] += 1

            # Update the highest frequency character count
            if freq[idx] > max_freq:
                max_freq = freq[idx]

            # Check if window is invalid
            window_size = right - left + 1
            if window_size - max_freq > k:
                freq[ord(s[left]) - 65] -= 1
                left += 1
                window_size -= 1  # Update window size after shrinking

            # Update max_length with valid window
            if window_size > max_length:
                max_length = window_size

        return max_length





 