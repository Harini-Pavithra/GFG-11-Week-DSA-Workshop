Largest subarray with 0 sum 

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 104
-1000 <= A[i] <= 1000, for each valid i

Solution

#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    #Code here
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}

    # Initialize result
    max_len = 0

    # Initialize sum of elements
    curr_sum = 0

    # Traverse through the given array
    for i in range(len(arr)):

        # Add the current element to the sum
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1

        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Look if current sum is seen
        # before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:

            # else put this sum in dictionary
            hash_map[curr_sum] = i

    return max_len
    return max1



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends