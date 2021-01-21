Remainder with 7 

Given a number as string(n) , find the remainder of the number whe it is divided by 7

Example 1:

Input:
5
Output:
5
 

Example 2:

Input:
8
Output:
1
 

Your Task:

You only need to complete the function remainderwith7() that takes string n as parameter and returns an integer which denotes the remainder of the number when its divided by 7

 

Constraints:
1<=T<=100
1<=length of n <=300
 
Solution

#your task is to complete this function
#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(str):
    #Code here
    r = int(str)%7
    return r
    



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends