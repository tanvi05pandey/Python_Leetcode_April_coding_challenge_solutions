# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that
# is common to both strings.
#
# If there is no common subsequence, return 0
#
# Example 1:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

def longestCommonSubsequence(text1, text2):
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

    text1 = " " + text1
    text2 = " " + text2

    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

print(longestCommonSubsequence('abcde', 'ace'))