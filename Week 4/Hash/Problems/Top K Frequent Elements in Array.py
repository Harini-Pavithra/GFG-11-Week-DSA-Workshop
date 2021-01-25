Top K Frequent Elements in Array - | 

Given a non-empty array of integers, find the top K elements which have the highest frequency in the array. If two numbers have the same frequency then the larger number should be given preference. 

Example 1:

Input:
N = 6
A[] = {1,1,1,2,2,3}
K = 2
Output: 1 2
Example 2:

Input:
N = 8
A[] = {1,1,2,2,3,3,3,4}
K = 2
Output: 3 2
Explanation: Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 > 1.
User Task:
The task is to complete the function TopK() that takes the array and integer K as input and returns a list of top K frequent elements.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 103
1<=A[i]<=104

Solution

#User function Template for python3

# arr[] : input list of size n
# k     : as specified in the problem description
# Return a list that consists of the Top K most frequent elements in arr
def TopK(arr, n, k): 
    um = {} 
    for i in range(n): 
        if arr[i] in um: 
            um[arr[i]] += 1
        else: 
            um[arr[i]] = 1
    a = [0] * (len(um)) 
    j = 0
    for i in um: 
        a[j] = [i, um[i]] 
        j += 1
    a = sorted(a, key = lambda x : x[0], 
                         reverse = True) 
    a = sorted(a, key = lambda x : x[1],  
                         reverse = True) 
                     
                     
    res = []      
    for i in range(k): 
        res.append (a[i][0])
        
    return res
  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())

for tc in range (t):
    inp = list(map(int, input().split()))
    n = inp[0]
    arr = inp[1:]
    k = int (input ())
    
    res = TopK (arr, n, k)
    
    for i in res:
        print (i, end = " ")
        
    print ()
    
# Contributed By : Pranay Bansal
# } Driver Code Ends
