Print Non-Repeated Elements 

Hashing is very useful to keep track of the frequency of the elements in a list.

You are given an array of integers. You need to print the non-repeated elements as they appear in the array.

Example 1:

Input:
n = 10
arr[] = {1,1,2,2,3,3,4,5,6,7}
Output: 4 5 6 7
Explanation: 4, 5, 6 and 7 are the only 
elements which is having only 1 
frequency and hence, Non-repeating.
Example 2:

Input:
n = 5
arr[] = {10,20,40,30,10}
Output: 20 40 30
Explanation: 20, 40, 30 are the only 
elements which is having only 1 
frequency and hence, Non-repeating.
Your Task:
You don't need to read input or print anything. You only need to complete the function printNonRepeated() that takes arr and n as parameters and return the array which has the distinct elements in same order as they appear in input array. The newline is appended automatically by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 103
0 <= arri <= 107

Solution

#User function Template for python3


#Complete this function
def printNonRepeated(arr,n):
    #Your code here
    dict={}
    for i in arr:
        dict[i]=0
        
    # iterating through the elements 
    for i in arr:
        dict[i]+=1
    
    # iterating through the elements 
    # and print if its occurrence is 1
    l = []
    for i in arr:
        if dict[i]==1:
            l.append(i)
    return l
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        l = printNonRepeated(arr,n)
        print(*l)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends