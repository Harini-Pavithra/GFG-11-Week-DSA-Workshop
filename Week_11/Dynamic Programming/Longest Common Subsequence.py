Longest Common Subsequence

Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Example 1:

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
Example 2:

Input:
A = 3, B = 2
str1 = ABC
str2 = AC
Output: 2
Explanation: LCS of "ABC" and "AC" is
"AC" of length 2.
Your Task:
Complete the function lcs() which takes the length of two strings respectively and two strings as input parameters and returns the length of the longest subsequence present in both of them.

Expected Time Complexity : O(|str1|*|str2|)
Expected Auxiliary Space: O(|str1|*|str2|)

Constraints:
1<=size(str1),size(str2)<=103

Solution

class Solution:
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        #using dp[][] array to store length of LCS.
        dp = [[None] * (y + 1) for i in range(x + 1)]
    
        #Following steps build dp[x+1][y+1] in bottom up fashion. Note that 
        #dp[i][j] contains length of LCS of s1[0..i-1] and s2[0..j-1].
        for i in range(x + 1):
            for j in range(y + 1):
                
                #if i or j is 0, we mark dp[i][j] as 0. 
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                #else if the current char in both strings are equal, we add 1 
                #to the output we got without including these both characters.
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                #else s1[i-1]!=s2[j-1] so we check the max output which 
                #comes from s1 or s2 without considering current character.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        #returning the result.            
        return dp[x][y]
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends