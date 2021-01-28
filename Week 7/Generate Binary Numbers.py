Generate Binary Numbers 

Given a number N. The task is to generate and print all binary numbers with decimal values from 1 to N.

Example 1:

Input:
N = 2
Output: 
1 10
Explanation: 
Binary numbers from
1 to 2 are 1 and 10.

Example 2:

Input:
N = 5
Output: 
1 10 11 100 101
Explanation: 
Binary numbers from
1 to 5 are 1 , 10 , 11 , 100 and 101.
 

Your Task:
You only need to complete the function generate() that takes N as parameter and returns vector of strings denoting binary numbers.

Expected Time Complexity : O(N log2N)
Expected Auxilliary Space : O(N log2N)

Constraints:
1 ≤ N ≤ 106

Solution:

#User function Template for python3
'''
Function Arguments :
		@param  : n (given number)
		@return : list of all the binary numbers till n.
'''
def generate(N):
    # code here
    queue = []
    for i in range(1,N+1):
        str1=""
        while(i):
            # print(queue)
            r=i%2
            str1=str1+str(r)
            i=i//2
        str1 = str1[::-1]
        queue.append(str1)
    return queue




#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by :  Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends
