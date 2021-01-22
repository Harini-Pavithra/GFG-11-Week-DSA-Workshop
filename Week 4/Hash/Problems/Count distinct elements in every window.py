Count distinct elements in every window 

Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1
Your Task:
Your task is to complete the function countDistinct() which takes the array A[], the size of the array(N) and the window size(K) as inputs and returns an array containing the count of distinct elements in every contiguous window of size K in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= K <= 105
1 <= A[i] <= 105 , for each valid i

Solution

from collections import defaultdict

def countDistinct(arr, N, K):
    # Code here
    # Creates an empty hashmap mp
	mp = defaultdict(lambda:0)
	# initialize distinct element 
	# count for current window 
	dist_count = 0
	# Traverse the first window and store count 
	# of every element in hash map 
	for i in range(k): 
		if mp[arr[i]] == 0: 
			dist_count += 1
		mp[arr[i]] += 1
		
	res = []
	# Print count of first window 
	res.append (dist_count)
	
	# Traverse through the remaining array 
	for i in range(k, n): 

		# Remove first element of previous window 
		# If there was only one occurrence, 
		# then reduce distinct count. 
		if mp[arr[i - k]] == 1: 
			dist_count -= 1
		mp[arr[i - k]] -=1
	
	# Add new element of current window 
	# If this element appears first time, 
	# increment distinct element count 
		if mp[arr[i]] == 0: 
			dist_count += 1
		mp[arr[i]] += 1

		# Print count of current window 
		res.append (dist_count)
		
	return res

    



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends