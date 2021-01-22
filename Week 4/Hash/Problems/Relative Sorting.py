Relative Sorting

Given two integer arrays. Sort the first array such that all the relative positions of the elements in the first array are the same as the elements in the second array.
See example for better understanding.

Example 1:

Input:
N = 11, M = 4
A1[] = {2,1,2,5,7,1,9,3,6,8,8}
A2[] = {2,1,8,3}
Output: 2 2 1 1 8 8 3 5 6 7 9
Explanation: Array elements of A1[] are
sorted according to A2[]. So 2 comes first
then 1 comes, then comes 8, then finally 3
comes, now we append remaining elements in
sorted order.
Example 2:

Input:
N = 11, M = 4
A1[] = {2,1,2,5,7,1,9,3,6,8,8}
A2[] = {99,22,444,56}
Output: 1 1 2 2 3 5 6 7 8 8 9
Explanation: No A2 elements are in A1
so we cannot sort A1 according to A2.
Hence we sort the elements in 
non-decreasing order.
Input:
The first line of input contains the number of test cases. For each testcase, the first line of input contains the length of arrays N and M and the next two lines contain N and M elements respectively. 

Output:
For each testcase, in a new line, print the elements of A1 sorted relatively according to A2.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortA1ByA2() which takes the array A1[], array A2[] and their respective size N and M as inputs and sorts the array A1[] such that the relative positions of the elements in A1[] are same as the elements in A2[]. For the elements not present in A2[] but in A1[], it appends them at the last in increasing order. 

Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N,M  ≤ 106
1 ≤ A1[], A2[] <= 106

Solution

#User function Template for python3

# A1[] : the input array-1
# N : size of the array A1[]
# A2[] : the input array-2
# M : size of the array A2[]

def relativeSort (A1, N, A2, M):
    # Your Code Here
    d={}
    for i in a1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=[]
    an=[]
    arr=set(a1)-set(a2)
    for i in arr:
        if i in d:
            an.extend([i]*d[i])
    for i in a2:
        if i in d:
            ans.extend([i]*d[i])
    ll=list(an)
    ll.sort()
    ans.extend(ll)
    
    return ans
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
while t > 0:
    n, m = list(map(int, input().split()))
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    
    a1 = relativeSort (a1, n, a2, m)
    for i in a1:
        print (i, end = " ")
    
    print ()
    
    t -= 1
    
# } Driver Code Ends