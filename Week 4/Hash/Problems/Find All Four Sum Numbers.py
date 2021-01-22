Find All Four Sum Numbers

Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 $
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
Example 2:

Input:
N = 7, K = 23
A[] = {10,2,3,4,5,7,8}
Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
Explanation: Sum of 2, 3, 8, 10 = 23,
sum of 2, 4, 7, 10 = 23 and sum of 3,
5, 7, 8 = 23.
Your Task:
You don't need to read input or print anything. Your task is to complete the function fourSum() which takes the array arr[] and the integer k as its input and returns an array containing all the quadruples in a lexicographical manner. Also note that all the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.  (In the output each quadruple is separate by $. The printing is done by the driver's code)

Expected Time Complexity: O(N3).
Expected Auxiliary Space: O(N2).

Constraints:
1 <= N <= 100
-1000 <= K <= 1000
-100 <= A[] <= 100

Solution

#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required

def fourSum(arr, k):
    # code here
    n=len(a)
    ans=[]
    if(n < 4):
        return ans
    a.sort()
    for i in range(0, n-3):
        # current element is greater than k then no quadruplet can be found
        if (a[i] > 0 and a[i] > k):
            break
        # removing duplicates
        if (i > 0 and a[i] == a[i - 1]):
            continue
        
        for j in range(i+1, n-2):
            # removing duplicates
            if (j > i + 1 and a[j] == a[j - 1]):
                continue

            # taking two pointers
            left = j + 1
            right = n - 1
            while (left < right):
                old_l = left;
                old_r = right;
                # calculate current sum
                sum = a[i] + a[j] + a[left] + a[right]
                if (sum == k):
                    # add to answer
                    ans.append([a[i], a[j], a[left], a[right]])

                    # removing duplicates
                    while (left < right and a[left] == a[old_l]):
                        left+=1
                    while (left < right and a[right] == a[old_r]):
                        right-=1
                elif (sum > k):
                    right-=1
                else:
                    left+=1
                
    return ans;




#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ans=fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends 