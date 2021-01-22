Sorting Elements of an Array by Frequency 

Given an array of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.

Example 1:

Input:
N = 5
A[] = {5,5,4,6,4}
Output: 4 4 5 5 6
Explanation: The highest frequency here is
2. Both 5 and 4 have that frequency. Now
since the frequencies are same then 
smallerelement comes first. So 4 4 comes 
firstthen comes 5 5. Finally comes 6.
The output is 4 4 5 5 6.
Example 2:

Input:
N = 5
A[] = {9,9,9,2,5}
Output: 9 9 9 2 5
Explanation: The highest frequency here is
3. The element 9 has the highest frequency
So 9 9 9 comes first. Now both 2 and 5
have same frequency. So we print smaller
element first.
The output is 9 9 9 2 5.
Your Task:

You only need to complete the function sortByFreq that takes arr, and n as parameters and returns the sorted array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N). 

Constraints:
1 ≤ N ≤ 105
1 ≤ Ai ≤ 105 

Solution

#User function Template for python3
'''
	Your task is to sort the elements according
	to the frequency of their occurence
	in the given array.
	
	Function Arguments: array a with size n. 
	Return Type:Array, the sorted array

'''
def sortByFreq(a,n):
    #code here
    #list containing frequency of all elements present in array a
    freq=[0 for i in range(max(a)+1)]

    #list of elements with frequency 'i' in array at index i.
    hash_for_freq=[ [] for i in range(n+1) ]

    for num in a:
        freq[num]+=1
    for i in range(max(a)+1):
        if(freq[i]):
            hash_for_freq[freq[i]].append(i)

    # here the complexity of this block of code can be proved to be O(n).
    l = []
    for i in range(n,0,-1):
        for num in hash_for_freq[i]:
            for j in range(i):
                l.append(num)
    return l

    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        l = sortByFreq(a,n)
        print(*l)
# } Driver Code Ends