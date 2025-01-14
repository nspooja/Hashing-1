## Problem 2:
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = t[i]
            else:
                if sMap[s[i]] != t[i]:
                    return False

            if t[i] not in tMap:
                tMap[t[i]] = s[i]
            else:
                if tMap[t[i]] != s[i]:
                    return False

        return True

