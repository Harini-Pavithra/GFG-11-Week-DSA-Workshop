Smallest divisible number 

Given a number N, find an integer denoting the smallest number evenly divisible by each number from 1 to n.


Example 1:

Input:
N = 3
Output: 6
Explanation: 6 is the smallest number 
divisible by 1,2,3.

Example 2:

Input:
N = 6
Output: 60
Explanation: 60 is the smallest number 
divisible by 1,2,3,4,5,6.

Your Task:  
You dont need to read input or print anything. Complete the function getSmallestDivNum() which takes N as input parameter and returns the smallest number evenly divisible by each number from 1 to n.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 25

Code:

#User function Template for python3
import math
class Solution:
    def getSmallestDivNum(self, n): # code here 
        result = 1
        for i in range(1,n+1):
            result = int((result * i)//math.gcd(result, i))
        return result
        
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob = Solution()
        print(ob.getSmallestDivNum(n))
# } Driver Code Ends