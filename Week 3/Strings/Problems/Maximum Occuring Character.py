Maximum Occuring Character

Given a string str. The task is to find the maximum occurring character in the string str. If more than one character occurs the maximum number of time then print the lexicographically smaller character.

Example 1:

Input:
str = testsample
Output: e
Explanation: e is the character which
is having the highest frequency.
Example 2:

Input:
str = output
Output: t
Explanation:  t and u are the characters
with the same frequency, but t is
lexicographically smaller.
Your Task:
The task is to complete the function getMaxOccuringChar() which returns the character which is most occurring.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |s|

Constraints:
1 ≤ |s| ≤ 100

Solution

#User function Template for python3


'''
	Your task is to return the lexicographically smallest 
	max occuring charcter in given string.
	
	Function Arguments: s (given string)
	Return Type: char or -1.
	
'''

def getMaxOccurringChar(s):
    #code here
    max1 = 0
    maxchar = s[0]
    for i in range(len(s)):
        c=0
        for j in range(len(s)):
            if s[i] == s[j]:
                c=c+1

        if ((c>=max1) and (maxchar >= s[i])):
            max1=c
            maxchar = s[i]
        #print(s[i])
    # print(max1,maxchar)
    return maxchar



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(getMaxOccurringChar(s))
# } Driver Code Ends

