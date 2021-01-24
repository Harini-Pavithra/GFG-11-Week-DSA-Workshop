Max rectangle

Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Example 1:

Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.
Your Task: 
Your task is to complete the function maxArea which returns the maximum size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two integers n and m which denotes the size of the matrix M. 

Expected Time Complexity : O(n*m)
Expected Auixiliary Space : O(m)

Constraints:
1<=n,m<=1000
0<=M[][]<=1

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.


Solution:

#User function Template for python3


# Finds the maximum area under the histogram represented 
# by histogram. See below article for details. 
# https:#www.geeksforgeeks.org/largest-rectangle-under-histogram/ 
def maxHist(row, C): 

	# Create an empty stack. The stack holds 
	# indexes of hist array/ The bars stored 
	# in stack are always in increasing order 
	# of their heights. 
	result = list()

	top_val = 0	 # Top of stack 

	max_area = 0 # Initialize max area in current 
				# row (or histogram) 

	area = 0 # Initialize area with current top 

	# Run through all bars of given 
	# histogram (or row) 
	i = 0
	while (i < C): 
	
		# If this bar is higher than the 
		# bar on top stack, push it to stack 
		if (len(result) == 0) or (row[result[-1]] <= row[i]): 
			result.append(i) 
			i += 1
		else: 
		
			# If this bar is lower than top of stack, 
			# then calculate area of rectangle with 
			# stack top as the smallest (or minimum 
			# height) bar. 'i' is 'right index' for 
			# the top and element before top in stack 
			# is 'left index' 
			top_val = row[result[-1]] 
			result.pop() 
			area = top_val * i 

			if (len(result)): 
				area = top_val * (i - result[-1] - 1 ) 
			max_area = max(area, max_area) 
		
	# Now pop the remaining bars from stack 
	# and calculate area with every popped 
	# bar as the smallest bar 
	while (len(result)): 
		top_val = row[result[-1]] 
		result.pop() 
		area = top_val * i 
		if (len(result)): 
			area = top_val * (i - result[-1] - 1 ) 

		max_area = max(area, max_area) 
	
	return max_area 

# Returns area of the largest rectangle 
# with all 1s in A 
def maxArea(A, R, C): 
	
	# Calculate area for first row and 
	# initialize it as result 
	result = maxHist(A[0], C) 

	# iterate over row to find maximum rectangular 
	# area considering each row as histogram 
	for i in range(1, R): 
	
		for j in range(C): 

			# if A[i][j] is 1 then add A[i -1][j] 
			if (A[i][j]): 
				A[i][j] += A[i - 1][j] 

		# Update result if area with current 
		# row (as last row) of rectangle) is more 
		result = max(result, maxHist(A[i], C)) 
	
	return result 
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R, C = input().split()
        a=list(map(int,input().split()))
        j=0
        A=[]
        R=int(R)
        C=int(C)
        for i in range(0,R):
            A.append(a[j:j+C])
            j=j+C
        # print(A)
        print(maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends