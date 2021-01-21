Binary To Gray Code equivalent 

You are given a decimal number N. You need to find the gray code of the number N and convert it into decimal.
To see how it's done, refer here.

Example 1:

Input: N = 7
Output: 4
Explanation: 7 is represented as 111 in 
binary form. The gray code of 111 is 100, 
in the binary form whose decimal equivalent is 4.
Example 2:

Input: N = 10
Output: 15
Explanation: 10 is represented as 1010 in 
binary form. The gray code of 1010 is 1111, 
in the binary form whose decimal equivalent is 15.
Example 3:

Input: N = 0
Output: 0
Explanation: Zero is represented as zero 
in binary, gray, and decimal.

Your Task: The task is to complete the function greyConverter() which takes n as a parameter and returns it's equivalent gray code.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
0 <= N <= 109

Solution
#User function Template for python3

##Complete this fcuntion

def inversegrayCode(n):
    inv = 0;

    # Taking xor until
    # n becomes zero
    while (n):
        inv = inv ^ n;
        n = n >> 1;
    return inv;
def greyConverter(n):
    ##Your code here
     return n ^ (n >> 1)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(greyConverter(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends