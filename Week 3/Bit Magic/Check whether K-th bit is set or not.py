Check whether K-th bit is set or not

Given a number N and a bit number K, check if Kth bit of N is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.

Example 1:

Input: N = 4, K = 0
Output: false
Explanation: Binary representation of 4 is 100, 
in which 0th bit from LSB is not set. 
So, return false.
Example 2:

Input: N = 4, K = 2
Output: true
Explanation: Binary representation of 4 is 100, 
in which 2nd bit from LSB is set. 
So, return true.
Example 3:

Input: N = 500, K = 3
Output: false
Explanation: Binary representation of 500 is 
111110100, in which 3rd bit from LSB is not set. 
So, return false.

Your task:
You don't have to read input or print anything. Your task is to complete the function checkKthbit that takes n and k as parameters and returns either true (if kth bit is set) or false(if kth bit is not set).

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 109
0 ≤ K ≤ floor(log2(N) + 1)

Solution

#User function Template for python3

##Complete this code
def checkKthBit(n,k):
    #Your code here
    mask = 1<<k
    if mask&n>0:
        return True
    else:
        return False


#{ 
#Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends