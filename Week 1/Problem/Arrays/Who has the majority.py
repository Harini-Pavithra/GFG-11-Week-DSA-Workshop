Who has the majority? 

Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y. If both elements have the same frequency, then return the smaller element.
Note:  We need to return the element, not its count.

 

Example 1:

Input:
N = 11
arr[] = {1,1,2,2,3,3,4,4,4,4,5}
x = 4, y = 5
Output: 4
Explanation: 
frequency of 4 is 4.
frequency of 5 is 1.
 

Example 2:

Input:
N = 8
arr[] = {1,2,3,4,5,6,7,8}
x = 1, y = 7
Output: 1
Explanation: 
frequency of 1 is 1.
frequency of 7 is 1.
Since 1 < 7, return 1.
 

Your Task:
You don't need to read input or print anything. Complete the function majorityWins() that takes array, n, x, y as input parameters and return the element with higher frequency.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= n <= 103
0 <= arri , x , y <= 108

Solution:

#User function Template for python3

def majorityWins(arr, n,  x,y):
    # code here
    count =0
    count1=0
    for i in range(0,len(arr)):
        if arr[i]==x:
            count +=1
        else:
            if arr[i]==y:
                count1 +=1
    if count==count1:
        return min(x,y)
    else:
        if count > count1:
            return x
        else:
            return y


#{ 
#  Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends