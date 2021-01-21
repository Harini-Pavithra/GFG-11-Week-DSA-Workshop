Swap all odd and even bits 

Given an unsigned integer N. The task is to swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43(00101011). Here, every even position bit is swapped with adjacent bit on the right side(even position bits are highlighted in the binary representation of 23), and every odd position bit is swapped with an adjacent on the left side.

Example 1:

Input: N = 23
Output: 43
Explanation: 
Binary representation of the given number 
is 00010111 after swapping 
00101011 = 43 in decimal.
Example 2:

Input: N = 2
Output: 1
Explanation: 
Binary representation of the given number 
is 10 after swapping 01 = 1 in decimal.

Your Task: Your task is to complete the function swapBits() which takes an integer and returns an integer with all the odd and even bits swapped.


Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 109

Solution

#User function Template for python3


##Complete this function
def swapBits(n):
    #Your code here
    # Get all even bits of x
    even_bits = n & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = n & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return (even_bits | odd_bits)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

