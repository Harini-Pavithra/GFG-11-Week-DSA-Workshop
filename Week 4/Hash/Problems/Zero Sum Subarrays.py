Zero Sum Subarrays 

You are given an array A[] of size N. Find the total count of sub-arrays having their sum equal to 0.


Example 1:

Input:
N = 6
A[] = {0,0,5,5,0,0}
Output: 6
Explanation: The 6 subarrays are 
[0], [0], [0], [0], [0,0], and [0,0].

Example 2:

Input:
N = 10
A[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
Output: 4
Explanation: The 4 subarrays are [-1 -3 4]
[-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]

Your Task:
You don't need to read input or print anything. Complete the function findSubarray() that takes the array A and its size N as input parameters and returns the total number of sub-arrays with 0 sum. 
 

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)
 

Constraints:    
1<= N <= 107
-1010 <= Ai <= 1010

Solution

#User function Template for python3

def findSubArrays(arr,n):
    
    
    #return: count of sub-arrays having their sum equal to 0
    c=0
    hashMap = {} 
    out = [] 
    sum1 = 0
    for i in range(n):
        sum1 += arr[i] 
          
        if sum1 == 0: 
            out.append((0, i))
            c+=1
        al = [] 
          
        if sum1 in hashMap: 
              
            al = hashMap.get(sum1) 
            for it in range(len(al)): 
                out.append((al[it] + 1, i))
                c+=1
        al.append(i) 
        hashMap[sum1] = al 
    return c


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().strip().split(' ')]
        print(findSubArrays(A,N))
        
                
                
# } Driver Code Ends