Check if strings are rotations of each other or not

Given two strings s1 and s2. The task is to check if s2 is a rotated version of the string s1. The characters in the strings are in lowercase.

 

Example 1:

Input:
geeksforgeeks
forgeeksgeeks
Output: 
1
Explanation: s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.
 

Example 2:

Input:
mightandmagic
andmagicmigth
Output: 
0
Explanation: Here with any amount of
rotation s2 can't be obtained by s1.
 

Your Task:
The task is to complete the function areRotations() which checks if the two strings are rotations of each other. The function returns true if string 1 can be obtained by rotating string 2, else it returns false.

 

Expected Time Complexity: O(N).
Expected Space Complexity: O(N).
Note: N = |s1|.

 

Constraints:
1 <= |s1|, |s2| <= 107

Solution

#User function Template for python3

'''
	Your task is tocheck if the given two strings
	are rotations of each other.
	Function Arguments: s1 and s2 (given strings)
	Return Type:boolean
'''

def areRotations(s1,s2):
    #code here
    l1= list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    # print(l1,l2)
    if l1 == l2:
        return True
    else:
        return False




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
        s1=str(input())
        s2=str(input())
        if(areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends