Absolute Value

You are given an interger I, find the absolute value of the interger I.

 

Example 1:

Input:
I = -32
Output: 32
Explanation: 
The absolute value of -32 is 32.
 

Example 2:

Input:
I = 45
Output: 45
Explanation: 
The absolute value of 45 is 45 itself.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function absolute() which takes an integer I as input parameter and return the absolute value of I.

 

Expected Time Complexity: O(1)
Expected Auxiliary Space : O(1)

 

Constraints:
-106 <= I <= 106

Solution:
#{ 
#Driver Code Starts
# Initial Template for Python 3



 # } Driver Code Ends

# User function Template for python3
import math

def absolute(I):
    m=abs(I)
    return m
    # code here



#{ 
#Driver Code Starts.
def main():
    T = int(input()) #Input the number of testcases
    while(T > 0):
        I = int(input()) #input number
        print(absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases


if __name__ == "__main__":
    main()

#} Driver Code Ends