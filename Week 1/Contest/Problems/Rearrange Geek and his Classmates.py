Geek and his classmates are playing a prank on their Computer Science teacher. They change places every time the teacher turns to look at the blackboard. 

Each of the N students in the class can be identified by a unique roll number X and each desk has a number i associated with it. Only one student can sit on one desk. 
Each time the teacher turns her back, a student with roll number X sitting on desk number i gets up and takes the place of the student with roll number i.

If the current position of N students in the class is given to you in an array, such that i is the desk number and a[i] is the roll number of the student sitting on the desk, can you modify a[] to represent the next position of all the students ? 
 

Input:
The first line of the input contains an integer T denoting the number of testcases. The first line  of each test case contains an integer N, denoting the size of the array. The second line of each test case contains N space separated integers denoting the values arr[i] of the array.


Output:
For each test case, in a new line, print the elements of the modified array separated by spaces. 


Your Task:
You don't need to read input or print anything. Complete the function rearrange() that takes array and N as input parameters and modifies the array in-place to denote the next position of all the students.


Constraints:
1 <= T <= 10
1 <= N <= 10^5
0 <= arr[i] <= N-1


Example:

Sample Input:
2
6
0 5 1 2 4 3
5
4 3 2 1 0

Sample Output:
0 3 5 1 4 2 
0 1 2 3 4 

solution:
#User function Template for python3
import random
class Solution:	
	def rearrange(self, array, n):
		# code here
		#return random.shuffle(array)
		 
		  
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        array = list(map(int, input().strip().split(' ')))
        ob = Solution()
        ob.rearrange(array,n)
        for i in array:
            print(i,end=" ")
        print()
# } Driver Code Ends
