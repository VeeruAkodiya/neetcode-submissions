class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal Solution
        # Use Last occurrance insted of next occurance last seen updated in Dict.
        ans = 0
        left = 0
        last_occur = {}
        for index, ch in enumerate(s):
            left = max(left, last_occur.get(ch, -1) + 1)
            last_occur[ch] = index
            ans = max(ans, index - left + 1)
        return ans