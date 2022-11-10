#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(0, len(string)):
            if string[i] in last_idx:
                start_idx = max(start_idx, last_idx[string[i]] + 1)
    
            max_len = max(max_len, i-start_idx + 1)
    
            last_idx[string[i]] = i
        return max_len
