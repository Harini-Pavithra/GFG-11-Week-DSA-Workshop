Maximum subset XOR 

Given a set of positive integers. The task is to complete the function maxSubarrayXOR which returns an integer denoting the maximum XOR subset value in the given set.

Input Format:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains an integer N denoting the size of the array A[]. Then in the next line are N space separated values of the array.

Output Format:
For each test case in a new line output will be the maximum XOR subset value in the given set.

Your Task:
You need to complete the function maxSubarrayXOR.

Constraints:
1 <= T <= 100
1 <= N <= 50

Example:
Input:
2
3
2 4 5
3
9 8 5
Output:
7
13

Explanation:
Testcase1:
Input: set[] = {2, 4, 5}
Output: 7
The subset {2, 5} has maximum XOR value
Testcase2:
Input: set[] = {9, 8, 5}
Output: 13
The subset {8, 5} has maximum XOR value

Solution

# function to return maximum XOR subset in set[]
INT_BITS=32
   
# Function to return 
# maximum XOR subset 
# in set[] 
def maxSubarrayXOR(set,n): 
  
    # Initialize index of 
    # chosen elements 
    index = 0
   
    # Traverse through all 
    # bits of integer  
    # starting from the most 
    # significant bit (MSB) 
    for i in range(INT_BITS-1,-1,-1): 
      
        # Initialize index of 
        # maximum element and 
        # the maximum element 
        maxInd = index 
        maxEle = -2147483648
        for j in range(index,n): 
          
            # If i'th bit of set[j] 
            # is set and set[j] is  
            # greater than max so far. 
            if ( (set[j] & (1 << i)) != 0 
                     and set[j] > maxEle ): 
                  
                maxEle = set[j] 
                maxInd = j 
          
        # If there was no  
        # element with i'th 
        # bit set, move to 
        # smaller i 
        if (maxEle ==-2147483648): 
            continue
   
        # Put maximum element 
        # with i'th bit set  
        # at index 'index' 
        temp=set[index] 
        set[index]=set[maxInd] 
        set[maxInd]=temp 
   
        # Update maxInd and  
        # increment index 
        maxInd = index 
   
        # Do XOR of set[maxIndex] 
        # with all numbers having 
        # i'th bit as set. 
        for j in range(n): 
          
            # XOR set[maxInd] those 
            # numbers which have the 
            # i'th bit set 
            if (j != maxInd and
               (set[j] & (1 << i)) != 0): 
                set[j] = set[j] ^ set[maxInd] 
          
   
        # Increment index of 
        # chosen elements 
        index=index + 1
      
   
    # Final result is  
    # XOR of all elements 
    res = 0
    for i in range(n): 
        res =res ^ set[i] 
    return res 



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        print(maxSubarrayXOR(set,n))
# } Driver Code Ends