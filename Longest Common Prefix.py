# Longest Common Prefix

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        strs.sort()
        min_l = min(len(strs[0]), len(strs[-1]))

        for i in range(min_l):
            if(strs[0][i] != strs[-1][i]):
                return pref
            else:
                pref +=strs[0][i]
            
        return pref