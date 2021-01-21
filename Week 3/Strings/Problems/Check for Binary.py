Check for Binary 

Given a non-empty sequence of characters str, return true if sequence is Binary, else return false

Example 1:

Input:
str = 101
Output:
1
Explanation:
Since string contains only 0 and 1, output is 1.
Example 2:

Input:
str = 75
Output:
0
Explanation:
Since string contains digits other than 0 and 1, output is 0.
 

Your Task:
Complete the function isBinary() which takes an string str as input parameter and returns 1 if str is binary and returns 0 otherwise.

 

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)

Solution

# Return true if str is binary, else false
def isBinary(str):
    #code here
    for i in str:
        if i == '1' or i == '0':
            pass
        else:
            return False
    return True



#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends