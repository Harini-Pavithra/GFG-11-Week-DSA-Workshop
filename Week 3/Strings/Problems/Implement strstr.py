Implement strstr 

Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).

 

Example 1:

Input:
s = GeeksForGeeks, x = Fr
Output: -1
Explanation: Fr is not present in the
string GeeksForGeeks as substring.
 

Example 2:

Input:
s = GeeksForGeeks, x = For
Output: 5
Explanation: For is present as substring
in GeeksForGeeks from index 5 (0 based
indexing).
 

Your Task:
You don't have to take any input. Just complete the strstr() function which takes two strings str, target as an input parameter. The function returns -1 if no match if found else it returns an integer denoting the first occurrence of the x in the string s.

 

Expected Time Complexity: O(|s|*|x|)
Expected Auxiliary Space: O(1)

Note : Try to solve the question in constant space complexity.

 

Constraints:
1 <= |s|,|x| <= 1000

Solution

'''
	Your task is to return the index of the pattern
	present in the given string.
	
	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.
	
'''
def strstr(s,p):
    #code here
    ind_s = 0 # current index in s.

    while ind_s < len(s):
        if s[ind_s] == p[0] :
            ind_p = 0  # current index in p.
            temp_s = ind_s

            while temp_s < len(s) and s[temp_s] == p[ind_p]:
                ind_p += 1
                temp_s += 1

                if ind_p == len(p): # match is found at ind_s - temp_s.
                    return ind_s
        ind_s += 1
        
    return -1








#{ 
#  Driver Code Starts
#Contributed by : Nagendra Jha

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

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends