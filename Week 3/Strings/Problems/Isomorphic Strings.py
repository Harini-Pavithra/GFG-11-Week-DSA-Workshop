Isomorphic Strings 

Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 1
Explanation: There are two different
charactersin aab and xxy, i.e a and b
with frequency 2and 1 respectively.
Example 2:

Input:
str1 = aab
str2 = xyz
Output:
Explanation: There are two different
charactersin aab but there are three
different charactersin xyz. So there
won't be one to one mapping between
str1 and str2.
Your Task:
You don't need to read input or print anything.Your task is to complete the function areIsomorphic() which takes the string str1 and string str2 as input parameter and  check if two strings are isomorphic. The function returns true if strings are isomorphic else it returns false.

Expected Time Complexity: O(|str1|+|str2|).
Expected Auxiliary Space: O(Number of different characters).
Note: |s| represents the length of string s.

Constraints:
1 <= |str1|, |str2| <= 103

Solution

#User function Template for python3
'''
	Your task is to check if the given strings are
	isomorphic or not.
	
	Function Arguments: str1 and str2 (given strings)
	Return Type: boolean

'''
def areIsomorphic2(str1,str2):
    dict1 = {}
    len1 = len(str1)
    len2 = len(str2)
    # print(dict1,len1,len1)
    if len1 == len2:
        for  i in range(len1):
            if str1[i] in dict1.keys():
                    if dict1[str1[i]] == str2[i]:
                        pass
                    else:
                        return False
            else:
                dict1[str1[i]] = str2[i]
    else:
        return False
    return True

def areIsomorphic(s,p):
    first = areIsomorphic2(s, p)
    second = areIsomorphic2(p, s)
    # print(first, second)
    if (first == True and second == True):
        return True
    else:
        return False



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        p=str(input())
        if(areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends