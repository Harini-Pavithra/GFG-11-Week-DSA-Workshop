Passcode Protected

There are N houses in Geek valley numbered from 1 to N. Geek has installed a special lock system in all the houses where the numeric digits making up the house number are in order of their smallest numeric permutation. 
How many houses are passcode protected against danger ?

Input:
First line of input contains number of testcases T. For each testcase, there will a single input line containing N, the total number of houses in the valley.

Output:
Print the total number of houses that are passcode protected.

Your Task:
Complete the function passcode_protected() that takes N as input parameter and returns the number of houses that are protected by a lock.

Constraints: 
1 <= T <= 100
1 <= N <= (9 x 1017)

Example:
Sample Input:
2
13
666

Sample Output:
12
200

Explanation:
Testcase 1: Total houses in the valley = N = 13.
House numbers of protected house are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13. 
House number 10 can not be protected as the smallest permutation of the digits '0' and '1' is 01. 

Solution

#User function Template for python3
def findSmallestPermutation(num):
    nstr = str(num)
    lstr = list(nstr)
    lstr.sort()
    nstr = "".join(lstr)
    num = int(nstr)
    # print(nstr,num)
    return num
def passcode_protected(n):
    has_map = {}
    for i in range(1,n+1):
        smallestper= findSmallestPermutation(i)
        # print(smallestper)
        if smallestper in has_map.keys():
            pass
        else:
            has_map[smallestper] = True
    # print(has_map)
    # print(len(has_map))
    return len(has_map)

def countNumber(n):
	result = 0

	# Pushing 1 to 9 because all number
	# from 1 to 9 have this property.
	for i in range(1, 10):
		s = []
		if (i <= n):
			s.append(i)
			result += 1

		# take a number from stack and add
		# a digit smaller than last digit
		# of it.
		while len(s) != 0:
			tp = s[-1]
			s.pop()
			for j in range(tp % 10, 10):
				x = tp * 10 + j
				if (x <= n):
					s.append(x)
					result += 1

	return result



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(passcode_protected(n))
# } Driver Code Ends