## Problem 3:
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.



# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False

        pMap = {}
        sMap = {}
        words = str.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pMap:
                pMap[pattern[i]] = words[i]
            else:
                if pMap[pattern[i]] != words[i]:
                    return False

            if words[i] not in sMap:
                sMap[words[i]] = pattern[i]
            else:
                if sMap[words[i]] != pattern[i]:
                    return False

        return True