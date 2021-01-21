Bit Difference 

You are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert A to B.

Example 1:

Input: A = 10, B = 20
Output: 4
Explanation:
A  = 01010
B  = 10100
As we can see, the bits of A that need 
to be flipped are 01010. If we flip 
these bits, we get 10100, which is B.
Example 2:

Input: A = 20, B = 25
Output: 3
Explanation:
A  = 10100
B  = 11001
As we can see, the bits of A that need 
to be flipped are 10100. If we flip 
these bits, we get 11001, which is B.

Your Task: The task is to complete the function countBitsFlip() that takes A and B as parameters and returns the count of the number of bits to be flipped to convert A to B.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ A, B ≤ 106

Solution

#User function Template for python3

##Complete this function

def countBitsFlip(a,b):
    ##Your code here
    counter =0
    if a>b:
        a,b = b,a
    while(b>0):
        # print(a%2)
        if (a%2) == (b%2):
            pass
        else:
            counter = counter + 1
        a=a//2
        b=b//2
    return counter
import math
def countflip(a,b):
    num=a^b
    c=0
    while num>0:
        if num%2==1:
            c=c+1
        num=num//2
    return c



#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        print(countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
