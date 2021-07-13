Largest number with given sum 

Geek lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. He know that his password is the largest number of N digits that can be made with given sum S. As he is busy doing his homework, help him retrieving his password.

Example 1:

Input:
N = 5, S = 12
Output:
93000
Explanation:
Sum of elements is 12. Largest possible 
5 digit number is 93000 with sum 12.
Example 2:

Input:
N = 3, S = 29
Output:
-1
Explanation:
There is no such three digit number 
whose sum is 29.
Your Task : 
You don't need to read input or print anything. Your task is to complete the function largestNumber() which takes 2 integers N and S as input parameters and returns the password in the form of string, else return "-1" in the form of string.

Constraints:
1 ≤ N ≤ 104
0 ≤ S ≤ 9*104

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Solution

#User function Template for python3

class Solution:
    
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        
        #maximum achievable sum is 9*n. if given sum is 
        #greater than that, we return -1.
        if(9*n<s):
            return -1
        else:
            if n==1 or s==0:
                return s
                
            #calculating maximum number of nines we can get 
            #and adding them in string.
            nines = s//9
            s%=9 
            ans = '9'*nines
            
             #adding "0" in the string for remaining digits.
            if len(ans)<n:
                ans+=str(s)
                for i in range(n-nines-1): 
                    ans+='0' 
                    
                    
            #returning the final string.
            return ans
        
        
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends