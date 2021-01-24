Maximum Rectangular Area in a Histogram 

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation: 


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram 
will be 8  and there will be 2 consecutive 
histogram. And hence the area of the 
histogram will be 8x2 = 16.
Your Task:
The task is to complete the function getMaxArea() which takes the array arr[] and its size N as inputs and finds the largest rectangular area possible and returns the answer.

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 106
1 <= arr[i] <= 1012

Solution:

#User function Template for python3
'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''

def getMaxArea(histogram):
    #code here
    # This function calulates maximum  
    # rectangular area under given  
    # histogram with n bars 

    # Create an empty stack. The stack  
    # holds indexes of histogram[] list.  
    # The bars stored in the stack are 
    # always in increasing order of  
    # their heights. 
    stack = list()

    max_area = 0  # Initalize max area 

    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(histogram):

        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack 

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else:
            # pop the top 
            top_of_stack = stack.pop()

            # Calculate the area with  
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed 
            max_area = max(max_area, area)

            # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack:
        # pop the top 
        top_of_stack = stack.pop()

        # Calculate the area with  
        # histogram[top_of_stack]  
        # stack as smallest bar 
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        # update max area, if needed 
        max_area = max(max_area, area)

        # Return maximum area under  
    # the given histogram 
    return max_area



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(getMaxArea(a))
# } Driver Code Ends