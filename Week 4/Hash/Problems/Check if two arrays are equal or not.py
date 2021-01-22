Check if two arrays are equal or not 

Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

Example 1:

Input:
N = 5
A[] = {1,2,5,4,0}
B[] = {2,4,5,0,1}
Output: 1
Explanation: Both the array can be 
rearranged to {0,1,2,4,5}
Example 2:

Input:
N = 3
A[] = {1,2,5}
B[] = {2,4,15}
Output: 0
Explanation: A[] and B[] have only 
one common value.
Your Task:
Complete check() function which takes both the given array and their size as function arguments and returns true if the arrays are equal else returns false.The 0 and 1 printing is done by the driver code.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1<=N<=107
1<=A[],B[]<=1018

Solution

#User function Template for python3

def check(arr1, arr2, n):
    
    #return: True or False
    
    #code here
    dic1={}
    for i in arr1:
        try:
            if dic1[i] == 1:
                dic1[i] = dic1[i] + 1
        except:
            pass
        dic1[i] = 1
    # print(dic1)
    for i in arr2:
        try:
            dic1[i] = dic1[i] - 1
        except:
            pass
    # print(dic1)
    for i in dic1.keys():
        if dic1[i]!=0:
            return False
    return True
def check2(arr1, arr2, n):
    # return: True or False
    #method 1 sorting
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        n=int(input())
        
        arr1 = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        if check(arr1, arr2, n):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends