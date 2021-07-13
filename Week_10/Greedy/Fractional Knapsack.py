Fractional Knapsack

Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
 
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= W <= 105

Solution

#User function Template for python3

class Solution:
    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
       
        #taking variable for current weight in knapsack.
        curr_weight = 0
        curr_value = 0  
    
        #sorting items on basis of value/weight ratio.
        Items = sorted(Items, key = lambda x: (x.value/x.weight), reverse= True)
    
        #iterating over all the items.
        for i in range(n):
            
            #if currweight + itemâ€™s weight is less than or equal to W,
            #then we add the item's value to final value.
            if curr_weight+Items[i].weight <= W: 
                curr_weight += Items[i].weight
                curr_value += Items[i].value
                
            #else we take the fraction of the that item's value 
            #based on the remaining weight in knapsack.
            else:
                accomodate = W-curr_weight 
                value_added = Items[i].value *(accomodate/Items[i].weight)
                curr_value += value_added
                break 
            
        #returning final value.
        return curr_value

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends
