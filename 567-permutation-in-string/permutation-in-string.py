class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # Frequency array for s1
        s1_count = [0] * 26
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # Frequency array for the first window in s2
        window = [0] * 26
        for i in range(n):
            window[ord(s2[i]) - ord('a')] += 1

        # Count matches
        matches = sum(1 for i in range(26) if window[i] == s1_count[i])

        # Slide the window through s2
        for i in range(n, m):
            if matches == 26:
                return True

            # Add the new character
            new_char = ord(s2[i]) - ord('a')
            window[new_char] += 1
            if window[new_char] == s1_count[new_char]:
                matches += 1
            elif window[new_char] - 1 == s1_count[new_char]:
                matches -= 1

            # Remove the old character
            old_char = ord(s2[i - n]) - ord('a')
            window[old_char] -= 1
            if window[old_char] == s1_count[old_char]:
                matches += 1
            elif window[old_char] + 1 == s1_count[old_char]:
                matches -= 1

        return matches == 26


        

        