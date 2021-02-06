Merge k Sorted Arrays 

Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
Example 1:

Input:
K = 3
arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation:Above test case has 3 sorted
arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],[4, 5, 6], 
[7, 8, 9]]
The merged list will be 
[1, 2, 3, 4, 5, 6, 7, 8, 9].
Example 2:

Input:
K = 4
arr[][]={{1,2,3,4}{2,2,3,4},
         {5,5,6,6},{7,8,9,9}}
Output:
1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
Explanation: Above test case has 4 sorted
arrays of size 4, 4, 4, 4
arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4],
[5, 5, 6, 6]  [7, 8, 9, 9 ]]
The merged list will be 
[1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 
6, 6, 7, 8, 9, 9 ].
Your Task:
You do not need to read input or print anything. Your task is to complete mergeKArrays() function which takes 2 arguments, an arr[k][k] 2D Matrix containing k sorted arrays and an integer k denoting the number of sorted arrays, as input and returns the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python)

Expected Time Complexity: O(nk Logk)
Expected Auxiliary Space: O(k)

Constraints:
1 <= K <= 100

Solution

#User function Template for python3

class lst_entry:
    def __init__(self,x,y,z):
        self.val=x
        self.lst=y
        self.inx=z

class min_heap:
    def __init__(self):
        self.heap_lst=[]
    
    def add(self,x,y,z):
        self.heap_lst.append(lst_entry(x,y,z))
        index=len(self.heap_lst)-1
        while(index>0 and self.heap_lst[index].val < self.heap_lst[(index-1)//2].val):
            parent = (index-1)//2
            self.heap_lst[index] , self.heap_lst[parent] = self.heap_lst[parent] , self.heap_lst[index]
            index = parent
    
    def pop(self):
        ret=(self.heap_lst[0].val, self.heap_lst[0].lst, self.heap_lst[0].inx)
        l=len(self.heap_lst)
        self.heap_lst[0]=self.heap_lst[l-1]
        self.heap_lst.pop()
        l=l-1
        i=0
        while(1):
            if(2*i+1>=l):
                break
            child=2*i+1
            if(2*i+2<l and self.heap_lst[2*i+2].val < self.heap_lst[2*i+1].val):
                child=2*i+2
            if(self.heap_lst[child].val >= self.heap_lst[i].val):
                break
            self.heap_lst[i] , self.heap_lst[child] = self.heap_lst[child] , self.heap_lst[i]
            i=child
        return ret
    
    def available(self):
        if(len(self.heap_lst)>0):
            return True
        return False

def merge(numbers):
    n=len(numbers)
    h=min_heap()
    for i in range(n):
        h.add(numbers[i][0],i,0)
    arr=[]
    while(h.available()):
        val,i,j = h.pop()
        arr.append(val)
        if(j+1 < len(numbers[i]) ):
            h.add(numbers[i][j+1],i,j+1)
    return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        merged_list=merge(numbers)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends