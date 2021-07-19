Stickler Thief 

Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i] amount of money present in it.

Example 1:

Input:
n = 6
a[] = {5,5,10,100,10,5}
Output: 110
Explanation: 5+100+5=110
Example 2:

Input:
n = 3
a[] = {1,2,3}
Output: 4
Explanation: 1+3=4
Your Task:
Complete the function FindMaxSum() which takes an array arr[] and n as input which returns the maximum money he can get following the rules

Expected Time Complexity: O(N).
Expected Space Complexity: O(N).

Constraints:
1 ≤ n ≤ 104
1 ≤ a[i] ≤ 104

Solution

class Solution:
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        #storing sum up to current element including and 
        #excluding it in respective variables.
        incl_curr=a[0]
        excl_curr=0
        
        #storing sum up to previous element including and 
        #excluding it in respective variables.
        incl_prev=incl_curr
        excl_prev=excl_curr
        
        for i in range(1,n):
            
            #updating sum up to current element excluding it as maximum
            #of sum up to previous element excluding and including it.
            excl_curr=max(incl_prev,excl_prev)
            
            #updating sum up to current element including it as sum up to 
            #previous element excluding it + current element.
            incl_curr=excl_prev+a[i]
            
            #updating sum up to previous element including and 
            #excluding it for next iteration.
            excl_prev=excl_curr
            incl_prev=incl_curr
            
        #returning the maximum of sum up to current element  
        #including and excluding it.
        return max(excl_curr,incl_curr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends